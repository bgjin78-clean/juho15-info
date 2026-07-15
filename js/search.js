(function () {
  var articles = [
    { title: "근로장려금 신청방법", url: "/earned-income-credit.html", keywords: "근로장려금 장려금 홈택스" },
    { title: "근로장려금 2026 신청기간", url: "/earned-income-2026.html", keywords: "근로장려금 2026 신청기간 반기 정기" },
    { title: "근로장려금 단독 맞벌이 기준", url: "/earned-income-household.html", keywords: "근로장려금 단독 홑벌이 맞벌이 소득" },
    { title: "근로장려금 안내문 없이 신청", url: "/earned-income-no-letter.html", keywords: "근로장려금 안내문 없이" },
    { title: "자녀장려금 신청자격", url: "/child-tax-credit.html", keywords: "자녀장려금" },
    { title: "에너지바우처 신청방법", url: "/energy-voucher.html", keywords: "에너지바우처 난방 냉방" },
    { title: "청년내일저축계좌", url: "/youth-savings-account.html", keywords: "청년내일저축계좌 청년" },
    { title: "소상공인 지원금", url: "/small-business-support.html", keywords: "소상공인 지원금" },
    { title: "실업급여 신청방법", url: "/unemployment-benefit.html", keywords: "실업급여 고용보험" },
    { title: "자발적 퇴사 시 실업급여", url: "/unemployment-voluntary.html", keywords: "자발적 퇴사 실업급여 사직" },
    { title: "이직확인서 이직사유", url: "/unemployment-leaving-code.html", keywords: "이직확인서 이직사유 실업급여" },
    { title: "국가장학금 신청방법", url: "/national-scholarship.html", keywords: "국가장학금 장학금" },
    { title: "기초생활수급자 혜택", url: "/basic-livelihood.html", keywords: "기초생활수급자 생계급여" },
    { title: "주거급여 신청방법", url: "/housing-benefit.html", keywords: "주거급여 월세" },
    { title: "교육급여 신청대상", url: "/education-benefit.html", keywords: "교육급여" },
    { title: "차상위계층 혜택", url: "/near-poor-benefits.html", keywords: "차상위계층 차상위" },
    { title: "한부모가족 지원금", url: "/single-parent-support.html", keywords: "한부모가족" },
    { title: "장애수당 지원대상", url: "/disability-allowance.html", keywords: "장애수당" },
    { title: "장애인연금 신청방법", url: "/disability-pension.html", keywords: "장애인연금" },
    { title: "통신비 감면", url: "/telecom-discount.html", keywords: "통신비 감면 휴대폰" },
    { title: "전기요금 할인", url: "/electricity-discount.html", keywords: "전기요금 할인" },
    { title: "기초연금 수급자격", url: "/basic-pension.html", keywords: "기초연금 노인연금" },
    { title: "기초연금 탈락 재신청", url: "/basic-pension-rejection.html", keywords: "기초연금 탈락 재신청 소득인정액" },
    { title: "기초연금 소득인정액 계산", url: "/basic-pension-income.html", keywords: "기초연금 소득인정액 계산 재산" },
    { title: "부부 기초연금", url: "/basic-pension-couple.html", keywords: "부부 기초연금 감액" },
    { title: "국민연금 예상수령액", url: "/national-pension.html", keywords: "국민연금 연금" },
    { title: "국민연금 조기수령 연기수령", url: "/national-pension-early.html", keywords: "국민연금 조기수령 연기수령" },
    { title: "퇴직연금 조회방법", url: "/retirement-pension.html", keywords: "퇴직연금" },
    { title: "노인일자리 신청방법", url: "/senior-job.html", keywords: "노인일자리" },
    { title: "노인일자리와 기초연금", url: "/senior-job-basic-pension.html", keywords: "노인일자리 기초연금 활동비" },
    { title: "장기요양보험 등급", url: "/longterm-care.html", keywords: "장기요양보험 요양등급" },
    { title: "건강보험 환급금 조회", url: "/health-insurance-refund.html", keywords: "건강보험 환급금" },
    { title: "환급금 사칭 문자 구별", url: "/health-refund-scam.html", keywords: "환급금 사기 스미싱" },
    { title: "본인부담상한제 환급", url: "/health-copay-cap.html", keywords: "본인부담상한제 환급 시기" },
    { title: "에너지바우처 vs 전기할인", url: "/energy-vs-electricity.html", keywords: "에너지바우처 전기요금 할인 비교" },
    { title: "연말정산 환급 체크리스트", url: "/year-end-refund-tips.html", keywords: "연말정산 공제 환급 늘리기" },
    { title: "건강보험료 계산방법", url: "/health-insurance-premium.html", keywords: "건강보험료" },
    { title: "국가건강검진 대상자", url: "/medical-checkup.html", keywords: "건강검진" },
    { title: "국가암검진 대상자", url: "/cancer-screening.html", keywords: "암검진" },
    { title: "실손보험 청구방법", url: "/insurance-claim.html", keywords: "실손보험" },
    { title: "신용점수 조회방법", url: "/credit-score.html", keywords: "신용점수 신용등급" },
    { title: "자동차세 환급", url: "/car-tax-refund.html", keywords: "자동차세" },
    { title: "연말정산 환급금 조회", url: "/year-end-tax-refund.html", keywords: "연말정산 환급" },
    { title: "고용보험 가입이력 조회", url: "/employment-insurance.html", keywords: "고용보험" }
  ];

  var input = document.getElementById("site-search");
  var results = document.getElementById("search-results");
  if (!input || !results) return;

  input.addEventListener("input", function () {
    var q = input.value.trim().toLowerCase();
    results.innerHTML = "";
    if (!q) return;

    var matched = articles.filter(function (a) {
      return a.title.toLowerCase().indexOf(q) !== -1 || a.keywords.toLowerCase().indexOf(q) !== -1;
    }).slice(0, 8);

    matched.forEach(function (a) {
      var link = document.createElement("a");
      link.href = a.url;
      link.textContent = a.title;
      results.appendChild(link);
    });

    if (!matched.length) {
      results.textContent = "검색 결과가 없습니다.";
    }
  });
})();
