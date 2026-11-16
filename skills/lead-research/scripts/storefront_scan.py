#!/usr/bin/env python3
"""Qualify online stores against an ICP from their public storefront. Company level only.

Usage:
  python3 storefront_scan.py <urls.txt|accounts.csv> <lead-config.json> <out.csv> [--delay 1.5]

Input: a text file with one URL/domain per line, or a CSV with a `url` (or `domain`) column.
Config: JSON (see the skill's templates/lead-config.example.json): vertical keywords, rules, exclusions.

What it records (all public, business-level):
  platform, store id/name, custom domain, payment methods (COD?), commercial-registration /
  Saudi Business Center certificate / freelance-document presence, social account URLs, branded
  app + its App Store rating count, signals in the store's own text (e.g. manual order confirmation),
  vertical match, and a PASS / BORDERLINE / FAIL verdict with reasons.

What it deliberately does NOT record: email addresses, phone or WhatsApp numbers, or any person's
name. It only notes whether the store publishes a contact email and whether that email is on the
store's own domain, so a human can copy it from the storefront if the product's legal gate allows
(see the skill's compliance rules; e.g. Saudi CST rules ban automated address harvesting).
"""
import csv, json, re, sys, time, urllib.parse, urllib.request, urllib.robotparser

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
FREE_MAIL = {"gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com", "live.com", "msn.com", "outlook.sa", "hotmail.sa"}


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ar,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.geturl(), r.read().decode("utf-8", "ignore")


def robots_ok(url):
    p = urllib.parse.urlparse(url)
    rp = urllib.robotparser.RobotFileParser()
    try:  # fetch with a browser UA: the stdlib reader is blocked (403) by Cloudflare and then reads as "disallow all"
        _, body = fetch(f"{p.scheme}://{p.netloc}/robots.txt", timeout=15)
    except Exception:
        return True  # no readable robots.txt → no restriction stated
    rp.parse(body.splitlines())
    return rp.can_fetch("*", url)


def norm(u):
    u = u.strip()
    if not u:
        return None
    if not u.startswith("http"):
        u = "https://" + u
    return u.rstrip("/") + "/"


def salla_store(html):
    i = html.find('"twilight::init":')
    if i < 0:
        return None
    try:
        obj, _ = json.JSONDecoder().raw_decode(html[i + len('"twilight::init":'):])
        return obj.get("store") or {}
    except Exception:
        return {}


def platform_of(html):
    if '"twilight::init"' in html or "cdn.salla.sa" in html or "salla.network" in html:
        return "salla"
    if re.search(r"zid\.store|zidcdn|cdn\.zid", html):
        return "zid"
    if "cdn.shopify.com" in html or "Shopify.shop" in html:
        return "shopify"
    if "woocommerce" in html.lower():
        return "woocommerce"
    return "other"


def ios_rating_count(app_url):
    m = re.search(r"id(\d{6,})", app_url or "")
    if not m:
        return ""
    try:
        _, body = fetch(f"https://itunes.apple.com/lookup?id={m.group(1)}&country=sa")
        res = json.loads(body).get("results", [])
        return res[0].get("userRatingCount", 0) if res else ""
    except Exception:
        return ""


def email_kind(email, site_host):
    if not email or "@" not in email:
        return "none"
    dom = email.split("@", 1)[1].lower()
    host = site_host.lower().removeprefix("www.")
    if dom in FREE_MAIL:
        return "free-provider"
    if dom == host or host.endswith("." + dom) or dom.endswith("." + host):
        return "own-domain"
    return "other-domain"


def text_hits(text, words):
    return [w for w in words if w and w.lower() in text.lower()]


def scan(url, cfg):
    row = {"input_url": url, "fetched_url": "", "status": "", "platform": "", "store_id": "", "store_name": "",
           "custom_domain": "", "payments": "", "cod": "", "commercial_reg_published": "", "sbc_certificate": "",
           "freelance_doc": "", "contact_email_published": "", "contact_email_kind": "", "contact_phone_published": "",
           "social": "", "ios_app": "", "ios_ratings": "", "vertical": "", "signals": "", "verdict": "", "reasons": "",
           "contact_source": "", "scanned_at": time.strftime("%Y-%m-%d")}
    if not robots_ok(url):
        row.update(status="robots-disallow", verdict="SKIP", reasons="robots.txt disallows")
        return row
    try:
        final, html = fetch(url)
    except Exception as e:
        row.update(status=f"error: {type(e).__name__}", verdict="SKIP", reasons="fetch failed")
        return row
    row["fetched_url"], row["status"] = final, "ok"
    host = urllib.parse.urlparse(final).netloc
    row["platform"] = platform_of(html)
    st = salla_store(html) if row["platform"] == "salla" else None
    text = html
    if st:
        s = st.get("settings", {}) or {}
        contacts = st.get("contacts", {}) or {}
        pays = s.get("payments") or []
        row.update(store_id=st.get("id", ""), store_name=st.get("name", ""),
                   custom_domain="no" if "salla.sa/" in (st.get("url") or final) else "yes",
                   payments=",".join(pays), cod="yes" if "cod" in pays else "no",
                   commercial_reg_published="yes" if s.get("commercial_number") else "no",
                   sbc_certificate="yes" if (s.get("certificate") or {}).get("id") else "no",
                   freelance_doc="yes" if s.get("freelance_number") else "no",
                   contact_email_published="yes" if contacts.get("email") else "no",
                   contact_email_kind=email_kind(contacts.get("email"), host),
                   contact_phone_published="yes" if (contacts.get("mobile") or contacts.get("whatsapp")) else "no",
                   social=" ".join(v for v in (st.get("social") or {}).values() if v),
                   ios_app=(st.get("apps") or {}).get("appstore") or "",
                   contact_source=final)
        oi = " ".join(str(v) for v in (st.get("order_instruction") or {}).values())
        meta = " ".join(str(v) for v in (st.get("meta") or {}).values())
        text = " ".join([st.get("name", ""), str(st.get("description", "")), meta, oi])
        sig = text_hits(oi, cfg.get("signal_words_order_text", []))
        if sig:
            row["signals"] = "order text mentions: " + "/".join(sig)
    else:
        row["custom_domain"] = "yes" if not re.search(r"salla\.sa/|zid\.store/|myshopify\.com", final) else "no"
        row["cod"] = "unknown"
        row["contact_source"] = final
        title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
        desc = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', html, re.I)
        text = " ".join(x.group(1) for x in (title, desc) if x)  # visible identity only, not page code
    if row["ios_app"]:
        row["ios_ratings"] = ios_rating_count(row["ios_app"])
    verts = [v for v, words in cfg.get("verticals", {}).items() if text_hits(text, words)]
    row["vertical"] = "/".join(verts)

    rules, fails, soft = cfg.get("rules", {}), [], []
    if rules.get("platforms") and row["platform"] not in rules["platforms"]:
        fails.append(f"platform {row['platform']}")
    if rules.get("require_cod") and row["cod"] != "yes":
        (fails if row["cod"] == "no" else soft).append(f"COD {row['cod']}")
    if rules.get("require_custom_domain") and row["custom_domain"] != "yes":
        soft.append("no custom domain")
    mx = rules.get("max_ios_ratings")
    if mx is not None and isinstance(row["ios_ratings"], int) and row["ios_ratings"] >= mx:
        fails.append(f"branded app {row['ios_ratings']} ratings")
    if cfg.get("verticals") and not verts:
        soft.append("vertical not matched")
    ex = text_hits(text, cfg.get("exclude_words", []))
    if ex:
        fails.append("excluded: " + "/".join(ex))
    row["verdict"] = "FAIL" if fails else ("BORDERLINE" if soft else "PASS")
    row["reasons"] = "; ".join(fails + soft)
    return row


def read_inputs(path):
    if path.endswith(".csv"):
        with open(path, encoding="utf-8") as f:
            r = csv.DictReader(f)
            col = "url" if "url" in r.fieldnames else "domain"
            return [norm(x[col]) for x in r if x.get(col)]
    return [norm(l) for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    src, cfg_path, out = sys.argv[1:4]
    delay = float(sys.argv[sys.argv.index("--delay") + 1]) if "--delay" in sys.argv else 1.5
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    urls = [u for u in dict.fromkeys(read_inputs(src)) if u]
    rows = []
    for n, u in enumerate(urls, 1):
        rows.append(scan(u, cfg))
        print(f"[{n}/{len(urls)}] {rows[-1]['verdict']:<10} {u}  {rows[-1]['reasons']}", file=sys.stderr)
        time.sleep(delay)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    tally = {}
    for r in rows:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    print("yield:", tally, f"→ {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
