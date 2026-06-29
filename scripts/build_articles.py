#!/usr/bin/env python3
"""One-time site template builder for juho15.com article pages."""
import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://juho15.com"
UPDATE_DATE = "2026년 6월 29일"
AD_CLIENT = "ca-pub-5008748977607037"
AD_SLOT_TOP = "2318766489"
AD_SLOT_MID = "8085568257"
AD_SLOT_BOTTOM = "2318766489"

SKIP = {"index.html", "about.html", "privacy.html", "contact.html"}

META = {
    "basic-pension.html": {
        "related": [
            ("국민연금 예상수령액 조회방법", "/national-pension.html"),
            ("노인일자리 신청방법", "/senior-job.html"),
            ("장기요양보험 등급 신청방법", "/longterm-care.html"),
            ("기초생활수급자 혜택과 신청방법", "/basic-livelihood.html"),
        ],
        "official": [
            ("국민연금공단 기초연금", "https://www.nps.or.kr"),
            ("복지로 온라인 신청", "https://www.bokjiro.go.kr"),
        ],
    },
    "earned-income-credit.html": {
        "related": [
            ("자녀장려금 신청자격 안내", "/child-tax-credit.html"),
            ("연말정산 환급금 조회방법", "/year-end-tax-refund.html"),
            ("실업급여 신청조건과 신청방법", "/unemployment-benefit.html"),
            ("고용보험 가입이력 조회방법", "/employment-insurance.html"),
        ],
        "official": [("국세청 홈택스", "https://www.hometax.go.kr")],
    },
    "national-pension.html": {
        "related": [
            ("기초연금 수급자격 총정리", "/basic-pension.html"),
            ("근로장려금 신청방법", "/earned-income-credit.html"),
            ("건강보험 환급금 조회", "/health-insurance-refund.html"),
            ("에너지바우처 신청방법", "/energy-voucher.html"),
        ],
        "official": [("국민연금공단", "https://www.nps.or.kr")],
        "strip_patterns": [
            r"<h2>국민연금 예상수령액이란\?</h2>.*?(?=<h2>함께 보면 좋은 글</h2>|$)",
        ],
    },
}

DEFAULT_OFFICIAL = [("복지로", "https://www.bokjiro.go.kr")]

CATEGORY_RELATED = {
    "support": [
        ("근로장려금 신청방법", "/earned-income-credit.html"),
        ("기초연금 수급자격", "/basic-pension.html"),
        ("건강보험 환급금 조회", "/health-insurance-refund.html"),
        ("에너지바우처 신청방법", "/energy-voucher.html"),
    ],
    "welfare": [
        ("기초생활수급자 혜택", "/basic-livelihood.html"),
        ("차상위계층 확인방법", "/near-poor-benefits.html"),
        ("주거급여 신청방법", "/housing-benefit.html"),
        ("에너지바우처 신청방법", "/energy-voucher.html"),
    ],
    "pension": [
        ("기초연금 수급자격", "/basic-pension.html"),
        ("국민연금 예상수령액", "/national-pension.html"),
        ("노인일자리 신청방법", "/senior-job.html"),
        ("장기요양보험 등급", "/longterm-care.html"),
    ],
    "health": [
        ("건강보험 환급금 조회", "/health-insurance-refund.html"),
        ("건강보험료 계산방법", "/health-insurance-premium.html"),
        ("국가건강검진 대상자", "/medical-checkup.html"),
        ("연말정산 환급금 조회", "/year-end-tax-refund.html"),
    ],
}

FILE_CATEGORY = {
    "earned-income-credit.html": "support",
    "child-tax-credit.html": "support",
    "energy-voucher.html": "support",
    "youth-savings-account.html": "support",
    "small-business-support.html": "support",
    "unemployment-benefit.html": "support",
    "national-scholarship.html": "support",
    "basic-livelihood.html": "welfare",
    "housing-benefit.html": "welfare",
    "education-benefit.html": "welfare",
    "near-poor-benefits.html": "welfare",
    "single-parent-support.html": "welfare",
    "disability-allowance.html": "welfare",
    "disability-pension.html": "welfare",
    "telecom-discount.html": "welfare",
    "electricity-discount.html": "welfare",
    "basic-pension.html": "pension",
    "national-pension.html": "pension",
    "retirement-pension.html": "pension",
    "senior-job.html": "pension",
    "longterm-care.html": "pension",
    "health-insurance-refund.html": "health",
    "health-insurance-premium.html": "health",
    "medical-checkup.html": "health",
    "cancer-screening.html": "health",
    "insurance-claim.html": "health",
    "credit-score.html": "health",
    "car-tax-refund.html": "health",
    "year-end-tax-refund.html": "health",
    "employment-insurance.html": "health",
}


def extract_head(html: str) -> dict:
    title_m = re.search(r"<title>(.*?)</title>", html, re.S)
    desc_m = re.search(r'<meta name="description" content="(.*?)"', html)
    title = title_m.group(1).strip() if title_m else ""
    if " | 주호15" in title:
        title = title.split(" | 주호15")[0]
    desc = desc_m.group(1).strip() if desc_m else ""
    return {"title": title, "description": desc}


def extract_body(html: str) -> str:
    body_m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    if not body_m:
        return ""
    body = body_m.group(1).strip()
    body = re.sub(r"<p>\s*<a href=\"/\">홈으로.*?</p>", "", body, flags=re.S | re.I)
    body = re.sub(r"<h2>함께 보면 좋은 글</h2>\s*<ul>.*?</ul>", "", body, flags=re.S | re.I)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body


def ad_block(slot: str, layout: str = "auto") -> str:
    if layout == "in-article":
        return f"""<div class="ad-slot">
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="{AD_CLIENT}"
     data-ad-slot="{slot}"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>"""
    return f"""<div class="ad-slot">
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="{AD_CLIENT}"
     data-ad-slot="{slot}"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>"""


def build_page(filename: str, body: str, head: dict) -> str:
    slug = filename
    url = f"{SITE}/{slug}"
    title = head["title"]
    desc = head["description"]
    meta = META.get(filename, {})
    for pat in meta.get("strip_patterns", []):
        body = re.sub(pat, "", body, flags=re.S)

    cat = FILE_CATEGORY.get(filename, "support")
    related = meta.get("related") or CATEGORY_RELATED[cat]
    related = [r for r in related if not r[1].endswith(filename)][:4]
    official = meta.get("official", DEFAULT_OFFICIAL)

    related_html = "\n".join(f'<li><a href="{u}">{t}</a></li>' for t, u in related)
    official_html = "\n".join(f'<li><a href="{u}" rel="noopener noreferrer" target="_blank">{t}</a></li>' for t, u in official)

  # split body for mid ad - after 2nd h2
    parts = re.split(r"(?=<h2)", body, maxsplit=3)
    if len(parts) >= 3:
        intro = parts[0] + parts[1]
        rest = "".join(parts[2:])
    else:
        intro = body
        rest = ""

    ld_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": url,
        "dateModified": "2026-06-29",
        "author": {"@type": "Organization", "name": "주호15 인포"},
        "publisher": {"@type": "Organization", "name": "주호15 인포", "url": SITE},
    }, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={AD_CLIENT}" crossorigin="anonymous"></script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/png" href="/juho15-favicon.png">
<link rel="apple-touch-icon" href="/juho15-favicon.png">
<link rel="canonical" href="{url}">
<title>{title} | 주호15 인포</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="주호15 인포">
<meta property="og:locale" content="ko_KR">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">{ld_json}</script>
</head>
<body>

<header>
<div class="container">
<h1><a href="/">주호15 인포</a></h1>
<p class="tagline">정부지원금 · 복지혜택 · 연금 · 건강보험 · 생활정보</p>
</div>
</header>

<nav class="site-nav">
<div class="container">
<a href="/">홈</a>
<a href="/about.html">사이트소개</a>
<a href="/privacy.html">개인정보처리방침</a>
<a href="/contact.html">문의하기</a>
</div>
</nav>

<main class="container">

<nav class="breadcrumb" aria-label="breadcrumb">
<a href="/">홈</a> › {title}
</nav>

<article class="article-content">
{intro}
{ad_block(AD_SLOT_TOP, "in-article") if intro else ""}
{rest}
<div class="official-links">
<h2>공식 확인 링크</h2>
<ul>
{official_html}
</ul>
<p>신청 요건과 지원금액은 매년 변경될 수 있으므로 반드시 공식 사이트에서 최신 정보를 확인하세요.</p>
</div>
</article>

{ad_block(AD_SLOT_MID, "in-article")}

<section class="related-articles">
<h2>함께 보면 좋은 글</h2>
<ul>
{related_html}
</ul>
</section>

<div class="notice">
<strong>안내:</strong> 본 글은 이해를 돕기 위한 일반 정보이며, 법률·행정 해석을 대체하지 않습니다. 실제 신청 가능 여부와 지원금액은 관할 기관의 최신 안내를 확인하시기 바랍니다.
</div>

<p class="update-date">최종 업데이트: {UPDATE_DATE}</p>

{ad_block(AD_SLOT_BOTTOM)}

</main>

<footer>
<div class="container">
<p>
<a href="/about.html">사이트소개</a> |
<a href="/privacy.html">개인정보처리방침</a> |
<a href="/contact.html">문의하기</a>
</p>
<p>© juho15.com</p>
</div>
</footer>

</body>
</html>
"""


def main():
    for path in sorted(ROOT.glob("*.html")):
        if path.name in SKIP:
            continue
        html = path.read_text(encoding="utf-8")
        if "/css/site.css" in html:
            print(f"skip (already templated): {path.name}")
            continue
        head = extract_head(html)
        body = extract_body(html)
        out = build_page(path.name, body, head)
        path.write_text(out, encoding="utf-8")
        print(f"updated: {path.name}")


if __name__ == "__main__":
    main()
