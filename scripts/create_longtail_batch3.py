#!/usr/bin/env python3
"""Batch 3: ten new long-tail articles for active site maintenance."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.juho15.com"
UPDATE = "2026년 7월 22일"
UPDATE_ISO = "2026-07-22"
AD_CLIENT = "ca-pub-5008748977607037"

def ad(slot, layout="auto"):
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

ARTICLES = [
{
"file": "near-poor-application.html",
"title": "차상위계층 신청 방법과 필요 서류",
"desc": "차상위계층 인정 신청 절차, 유형별 요건, 행정복지센터 제출 서류, 기초수급과의 차이를 정리했습니다.",
"related": [
("차상위계층 확인방법과 혜택", "/near-poor-benefits.html"),
("기초수급 vs 차상위 차이", "/basic-livelihood-vs-near-poor.html"),
("주거급여 신청방법", "/housing-benefit.html"),
("에너지바우처 vs 전기요금 할인", "/energy-vs-electricity.html"),
],
"official": [("복지로", "https://www.bokjiro.go.kr")],
"intro": """<h1>차상위계층 신청 방법과 필요 서류</h1>
<p>차상위계층은 기초생활수급자는 아니지만 생활이 어려운 저소득 가구를 지원하는 제도입니다. <strong>인정만 받으면</strong> 의료·교육·주거·에너지 등 연계 혜택을 신청할 수 있습니다. 유형(한부모, 장애인, 자활근로 등)에 따라 서류가 달라집니다.</p>
""",
"rest": """<h2>신청은 어디서?</h2>
<ol>
<li>주소지 <strong>행정복지센터</strong> 방문</li>
<li>복지로 온라인 신청(가능 지역)</li>
<li>소득·재산 조사 후 차상위 인정</li>
</ol>
<h2>공통 준비 서류</h2>
<ul>
<li>신분증, 주민등록등본</li>
<li>소득·재산 관련 서류(통장, 임대차계약 등)</li>
<li>유형별 추가 서류(한부모 증명, 장애인등록증 등)</li>
</ul>
<h2>유형별 참고</h2>
<ul>
<li><strong>차상위계층</strong> — 소득 기준 충족 가구</li>
<li><strong>한부모·장애인·자활근로</strong> 등 세부 유형별 추가 요건</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>기초수급 탈락하면 차상위는?</h3>
<p>소득·재산 기준을 충족하면 차상위 인정이 가능할 수 있습니다.</p>
<h3>인정 후 혜택은 자동?</h3>
<p>의료·교육 등은 연계되지만, 전기·통신 할인은 별도 신청이 필요한 경우가 많습니다.</p>
""",
},
{
"file": "basic-livelihood-vs-near-poor.html",
"title": "기초수급 vs 차상위 차이와 선택 가이드",
"desc": "기초생활수급자와 차상위계층 소득 기준, 혜택 범위, 신청 순서, 동시 해당 여부를 비교해 정리했습니다.",
"related": [
("기초생활수급자 혜택", "/basic-livelihood.html"),
("차상위계층 신청 방법", "/near-poor-application.html"),
("주거급여 탈락 이유", "/housing-benefit-rejection.html"),
("에너지바우처 신청방법", "/energy-voucher.html"),
],
"official": [("복지로", "https://www.bokjiro.go.kr")],
"intro": """<h1>기초수급 vs 차상위 차이와 선택 가이드</h1>
<p>“기초수급은 안 되는데 생활이 어렵다”면 <strong>차상위계층</strong>을 확인해야 합니다. 두 제도는 소득 기준이 다르고, 받을 수 있는 혜택 범위도 다릅니다. 어느 쪽에 해당하는지 먼저 구분하세요.</p>
""",
"rest": """<h2>한눈에 비교</h2>
<table>
<tr><th>구분</th><th>기초생활수급</th><th>차상위계층</th></tr>
<tr><td>소득 기준</td><td>더 낮음(중위소득 약 30~50%)</td><td>기초수급 초과~중위소득 일정 %</td></tr>
<tr><td>생계급여</td><td>매월 현금 지원</td><td>원칙적으로 없음</td></tr>
<tr><td>의료·교육</td><td>의료급여·교육급여</td><td>본인부담 경감·교육급여 등</td></tr>
<tr><td>주거·에너지</td><td>주거급여 등 연계</td><td>주거·에너지바우처 등 별도</td></tr>
</table>
<h2>신청 순서 추천</h2>
<ol>
<li>기초생활수급 자격 먼저 상담·신청</li>
<li>탈락 시 차상위 해당 여부 확인</li>
<li>차상위 인정 후 전기·통신·주거 등 개별 혜택 신청</li>
</ol>
<h2>혼동하기 쉬운 점</h2>
<ul>
<li>차상위만으로는 생계급여가 없음</li>
<li>기초수급 중이면 차상위 신청 불필요</li>
<li>소득 변동 시 둘 다 재심사 가능</li>
</ul>
""",
},
{
"file": "housing-benefit-rejection.html",
"title": "주거급여 탈락 이유와 재신청 방법",
"desc": "주거급여 불승인 사유, 임차·자가별 기준, 소득인정액 초과, 이사·계약 변경 후 재신청 요령을 정리했습니다.",
"related": [
("주거급여 신청방법", "/housing-benefit.html"),
("기초수급 vs 차상위 차이", "/basic-livelihood-vs-near-poor.html"),
("차상위계층 신청 방법", "/near-poor-application.html"),
("기초연금 탈락 이유", "/basic-pension-rejection.html"),
],
"official": [("복지로", "https://www.bokjiro.go.kr")],
"intro": """<h1>주거급여 탈락 이유와 재신청 방법</h1>
<p>주거급여는 임차료·수선비를 지원하지만, <strong>소득인정액·주택 요건·계약서</strong> 중 하나라도 맞지 않으면 탈락합니다. “월세가 비싼데 왜 안 되나”는 대부분 기준 임대료 한도나 소득 문제입니다.</p>
""",
"rest": """<h2>탈락 흔한 이유</h2>
<ul>
<li>소득·재산 기준 초과</li>
<li>기준 임대료보다 실제 월세가 높음(초과분은 본인 부담)</li>
<li>임대차계약서·실거주 확인 불가</li>
<li>자가 주택인데 수선유지급여 요건 미충족</li>
<li>타 지역·타 가구원 정보 누락</li>
</ul>
<h2>재신청이 가능한 경우</h2>
<ul>
<li>소득 감소(실직, 연금만 수령 등)</li>
<li>가구원 변동(별거, 사별 등)</li>
<li>더 저렴한 주택으로 이전</li>
<li>계약 갱신·전입 신고 후 서류 보완</li>
</ul>
<h2>재신청 절차</h2>
<ol>
<li>탈락 통지 사유 확인</li>
<li>행정복지센터에 변경 사항 상담</li>
<li>새 임대차계약·소득 서류 제출</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>전세도 지원되나요?</h3>
<p>임차급여 내 전세 보증금 지원 한도가 있으며, 지역·가구원 수에 따라 다릅니다.</p>
""",
},
{
"file": "child-tax-2026.html",
"title": "자녀장려금 2026 신청 일정과 자격",
"desc": "자녀장려금 2026 정기·반기 신청 시기, 부양자녀 요건, 근로장려금과 함께 신청하는 방법을 정리했습니다.",
"related": [
("자녀장려금 신청자격", "/child-tax-credit.html"),
("근로장려금 2026 신청기간", "/earned-income-2026.html"),
("근로장려금 단독·맞벌이 기준", "/earned-income-household.html"),
("근로장려금 환수 대처", "/earned-income-repayment.html"),
],
"official": [("국세청 홈택스", "https://www.hometax.go.kr")],
"intro": """<h1>자녀장려금 2026 신청 일정과 자격</h1>
<p>자녀장려금은 양육 부담을 덜어주는 세제 지원금입니다. 근로장려금과 <strong>일정·신청 경로가 비슷</strong>하지만, 부양자녀 요건이 핵심입니다. 2026년에도 홈택스에서 정기·반기 신청을 확인하세요.</p>
""",
"rest": """<h2>2026 신청 시기(참고)</h2>
<ul>
<li><strong>정기신청</strong> — 보통 3~5월(전년도 소득 기준)</li>
<li><strong>반기신청</strong> — 상·하반기(근로소득자, 일정 요건)</li>
</ul>
<p>정확한 날짜는 국세청 공지가 기준입니다.</p>
<h2>자격 요약</h2>
<ul>
<li>만 18세 미만 부양자녀(일부 성인 자녀 포함 가능)</li>
<li>가구 소득·재산 기준 이하</li>
<li>거주·신고 요건 충족</li>
</ul>
<h2>근로장려금과 함께</h2>
<p>요건을 모두 충족하면 <strong>동시 신청·수급</strong>이 가능한 경우가 많습니다. 홈택스에서 한 번에 확인하세요.</p>
<h2>자주 묻는 질문</h2>
<h3>양육비를 받는데 신청되나요?</h3>
<p>가구 구성·소득 신고 방식에 따라 달라질 수 있습니다. 홈택스 안내를 따르세요.</p>
""",
},
{
"file": "longterm-care-grade-change.html",
"title": "장기요양 등급 변경·갱신 시기와 절차",
"desc": "장기요양보험 등급 유효기간, 상태 변화 시 재심사, 등급 하향·상향, 서비스 변경 방법을 정리했습니다.",
"related": [
("장기요양보험 등급 신청", "/longterm-care.html"),
("노인일자리와 기초연금", "/senior-job-basic-pension.html"),
("기초연금 수급자격", "/basic-pension.html"),
("국가건강검진 놓쳤을 때", "/medical-checkup-missed.html"),
],
"official": [("국민건강보험 장기요양", "https://www.longtermcare.or.kr")],
"intro": """<h1>장기요양 등급 변경·갱신 시기와 절차</h1>
<p>요양등급은 한 번 받으면 끝이 아닙니다. <strong>유효기간</strong>이 있고, 건강 상태가 나아지거나 악화되면 등급을 다시 심사해야 합니다. 서비스 시간·종류도 등급에 따라 달라집니다.</p>
""",
"rest": """<h2>등급 유효기간</h2>
<p>인정 등급은 보통 <strong>1~2년</strong> 유효하며, 만료 전 갱신·재심사 안내가 올 수 있습니다. 무시하면 서비스가 중단될 수 있습니다.</p>
<h2>등급 변경이 필요한 경우</h2>
<ul>
<li>치매·거동 상태가 악화(상향 필요)</li>
<li>재활·치료로 상태 호전(하향 가능)</li>
<li>유효기간 만료</li>
</ul>
<h2>신청·변경 절차</h2>
<ol>
<li>국민건강보험공단에 <strong>등급 변경·재심사</strong> 신청</li>
<li>방문 조사(인정조사) 재실시</li>
<li>판정위원회 심의 후 등급 결정</li>
<li>요양기관·방문요양 계획 조정</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>등급이 낮아지면 서비스가 줄어드나요?</h3>
<p>등급에 맞는 서비스 한도가 조정됩니다.</p>
""",
},
{
"file": "medical-checkup-missed.html",
"title": "국가건강검진 놓쳤을 때 재검진 방법",
"desc": "건강검진 기간을 놓친 경우 재검진·연기 신청, 대상 연도 확인, 직장·지역 검진 차이를 정리했습니다.",
"related": [
("국가건강검진 대상자", "/medical-checkup.html"),
("국가암검진 대상자", "/cancer-screening.html"),
("본인부담상한제 환급", "/health-copay-cap.html"),
("건강보험 환급금 조회", "/health-insurance-refund.html"),
],
"official": [("국민건강보험 건강검진", "https://www.nhis.or.kr")],
"intro": """<h1>국가건강검진 놓쳤을 때 재검진 방법</h1>
<p>국가건강검진은 <strong>연도별·연령별</strong>로 대상이 정해집니다. 기간을 놓겨도 바로 “내년에 하면 된다”고 단정하기 어렵습니다. 같은 해 재검진·다음 주기 확인이 필요합니다.</p>
""",
"rest": """<h2>먼저 확인할 것</h2>
<ol>
<li>The건강보험 앱에서 <strong>올해 대상 여부</strong></li>
<li>검진 기한(출생월·연령에 따라 다름)</li>
<li>직장검진과 국가검진 중복 여부</li>
</ol>
<h2>놓쳤을 때</h2>
<ul>
<li>일부 지역·기관에서 <strong>연말까지</strong> 예약 가능</li>
<li>대상 연도가 지나면 다음 주기까지 대기</li>
<li>암검진은 종류별 주기(2년 등)가 다름</li>
</ul>
<h2>재예약 방법</h2>
<ol>
<li>공단 앱·홈페이지에서 검진기관 선택</li>
<li>잔여 일정 확인 후 예약</li>
<li>직장에서 단체 검진 안내가 있으면 HR에 문의</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>회사 검진만 받으면 되나요?</h3>
<p>국가검진 대상이면 별도 제도입니다. 둘 다 해당되면 받는 것이 좋습니다.</p>
""",
},
{
"file": "retirement-pension-withdrawal.html",
"title": "퇴직연금 중도인출 가능 사유와 절차",
"desc": "DC·IRP 퇴직연금 중도인출 조건, 주택·의료·무주택 요건, 세금, 신청 서류를 정리했습니다.",
"related": [
("퇴직연금 조회방법", "/retirement-pension.html"),
("국민연금 조기·연기수령", "/national-pension-early.html"),
("주거급여 신청방법", "/housing-benefit.html"),
("연말정산 환급 체크리스트", "/year-end-refund-tips.html"),
],
"official": [("퇴직연금포털", "https://www.pension.or.kr")],
"intro": """<h1>퇴직연금 중도인출 가능 사유와 절차</h1>
<p>퇴직연금(DC·IRP)은 원칙적으로 <strong>만 55세 이후</strong> 수령하지만, 법에서 정한 사유가 있으면 <strong>중도인출</strong>이 가능합니다. 주택·의료 등 목적별로 한도와 요건이 다릅니다.</p>
""",
"rest": """<h2>중도인출 대표 사유</h2>
<ul>
<li><strong>무주택자 주택 구입·전세</strong> — 한도·횟수 제한</li>
<li><strong>6개월 이상 요양</strong> — 의료비 등</li>
<li><strong>회생·파산</strong> 등 법정 사유</li>
</ul>
<p>세부 한도는 연도별·계좌별로 다릅니다.</p>
<h2>신청 절차</h2>
<ol>
<li>퇴직연금 운용 금융기관(은행·증권) 문의</li>
<li>해당 사유 증빙 서류 준비</li>
<li>인출 신청·세금 원천징수 확인</li>
</ol>
<h2>주의할 점</h2>
<ul>
<li>중도인출분은 퇴직소득세 부과</li>
<li>노후 자금이 줄어드는 만큼 신중히 결정</li>
<li>IRP 추가 납입 한도와 별도 규정</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>그냥 생활비로 뺄 수 있나요?</h3>
<p>원칙적으로 불가합니다. 정해진 사유만 해당됩니다.</p>
""",
},
{
"file": "telecom-discount-documents.html",
"title": "통신비 감면 필요 서류와 신청처",
"desc": "기초수급·차상위·장애인 통신비 할인 신청 방법, 통신사별 제출 서류, 유선·이동 통신 구분을 정리했습니다.",
"related": [
("통신비 감면 신청방법", "/telecom-discount.html"),
("차상위계층 신청 방법", "/near-poor-application.html"),
("전기요금 할인 신청", "/electricity-discount.html"),
("에너지바우처 vs 전기 할인", "/energy-vs-electricity.html"),
],
"official": [("복지로", "https://www.bokjiro.go.kr")],
"intro": """<h1>통신비 감면 필요 서류와 신청처</h1>
<p>통신비 감면은 <strong>통신사</strong>에서 접수합니다. 복지 자격은 행정복지센터에서 확인하지만, 할인 적용은 SKT·KT·LG U+ 등 각 회사 고객센터·매장에서 진행합니다. 회선마다 신청해야 할 수 있습니다.</p>
""",
"rest": """<h2>대상자</h2>
<ul>
<li>기초생활수급자</li>
<li>차상위계층</li>
<li>장애인(등급별)</li>
<li>국가유공자 등</li>
</ul>
<h2>준비 서류</h2>
<ul>
<li>신분증</li>
<li>복지카드 또는 수급·차상위·장애 증명</li>
<li>통신 요금 청구서(고객번호 확인)</li>
</ul>
<h2>신청 방법</h2>
<ol>
<li>사용 중인 통신사 <strong>고객센터·매장</strong> 방문</li>
<li>할인 요금제·감면 등록</li>
<li>다음 달 요금부터 반영(회사별 상이)</li>
</ol>
<h2>유선·인터넷·휴대폰</h2>
<p>회선·상품마다 감면율이 다릅니다. 가족 명의 회선은 별도 신청이 필요할 수 있습니다.</p>
<h2>자주 묻는 질문</h2>
<h3>전기·가스 할인과 같이 자동?</h3>
<p>아닙니다. 통신사에 따로 신청해야 합니다.</p>
""",
},
{
"file": "national-pension-gap.html",
"title": "국민연금 가입 공백기와 추후납부 활용",
"desc": "국민연금 공백 기간 확인, 추후납부·임의계속가입, 예상연금액에 미치는 영향을 정리했습니다.",
"related": [
("국민연금 예상수령액 조회", "/national-pension.html"),
("국민연금 조기·연기수령", "/national-pension-early.html"),
("기초연금 수급자격", "/basic-pension.html"),
("고용보험 가입이력 조회", "/employment-insurance.html"),
],
"official": [("국민연금공단", "https://www.nps.or.kr")],
"intro": """<h1>국민연금 가입 공백기와 추후납부 활용</h1>
<p>취업 공백·육아·유학 등으로 국민연금 납부가 끊기면 <strong>가입 공백</strong>이 생깁니다. 공백이 길수록 예상연금이 줄어듭니다. <strong>추후납부</strong>·<strong>임의계속가입</strong>으로 메울 수 있는지 확인하세요.</p>
""",
"rest": """<h2>공백 확인 방법</h2>
<ol>
<li>국민연금공단 앱·홈페이지 로그인</li>
<li>가입이력·납부 이력 조회</li>
<li>미납·공백 월 확인</li>
</ol>
<h2>메우는 방법</h2>
<ul>
<li><strong>추후납부</strong> — 과거 미납·공백 기간 일시 또는 분할 납부</li>
<li><strong>임의계속가입</strong> — 소득 없는 기간 추가 가입(연령·요건)</li>
<li>재취업 시 직장·지역 가입자 전환</li>
</ul>
<h2>선택 시 고려</h2>
<ul>
<li>추후납부는 일시금 부담이 클 수 있음</li>
<li>납부해도 수령액 증가폭은 시뮬레이션으로 확인</li>
<li>기초연금 소득인정액과는 별도(납부는 재산·소득에 영향 가능)</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>군 복무 기간은?</h3>
<p>별도 제도(전역일 등)로 처리됩니다. 공단 조회로 확인하세요.</p>
""",
},
{
"file": "earned-income-repayment.html",
"title": "근로장려금 환수·오지급 발생 시 대처",
"desc": "근로장려금 지급 후 환수 통지, 소득·재산 신고 오류, 이의신청·분할납부, 자녀장려금 포함 안내를 정리했습니다.",
"related": [
("근로장려금 신청방법", "/earned-income-credit.html"),
("근로장려금 2026 신청기간", "/earned-income-2026.html"),
("자녀장려금 2026 일정", "/child-tax-2026.html"),
("근로장려금 단독·맞벌이 기준", "/earned-income-household.html"),
],
"official": [("국세청 홈택스", "https://www.hometax.go.kr")],
"intro": """<h1>근로장려금 환수·오지급 발생 시 대처</h1>
<p>장려금을 받은 뒤 <strong>소득·재산이 늘거나 신고 오류</strong>가 발견되면 환수 통지가 올 수 있습니다. “이미 썼는데”라도 국세청 정산 결과를 따라야 합니다. 이의가 있으면 기한 내 절차를 밟으세요.</p>
""",
"rest": """<h2>환수가 발생하는 경우</h2>
<ul>
<li>신청 후 소득·재산 신고 누락·과소 신고</li>
<li>가구원 정보 변경 미반영</li>
<li>타 소득(퇴직·상속·매매 등) 발생</li>
<li>자녀장려금·근로장려금 동시 정산 오류</li>
</ul>
<h2>통지를 받으면</h2>
<ol>
<li>환수 사유·금액 확인(홈택스·우편)</li>
<li>사실과 다르면 <strong>이의신청</strong> 기한 확인</li>
<li>맞다면 납부·분할 납부 가능 여부 문의</li>
</ol>
<h2>예방</h2>
<ul>
<li>가구·소득 변동 시 즉시 정정 신고</li>
<li>반기·정기 신청 시 최신 자료 입력</li>
<li>허위 신청은 가산세·추징 대상</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>못 갚으면?</h3>
<p>분할 납부·징수 유예 등은 국세청 기준에 따릅니다. 상담 전화(126)를 활용하세요.</p>
""",
},
]


def build_page(a):
    url = f"{SITE}/{a['file']}"
    related = "\n".join(f'<li><a href="{u}">{t}</a></li>' for t, u in a["related"])
    official = "\n".join(
        f'<li><a href="{u}" rel="noopener noreferrer" target="_blank">{t}</a></li>'
        for t, u in a["official"]
    )
    ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["desc"],
        "url": url,
        "dateModified": UPDATE_ISO,
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
<title>{a['title']} | 주호15 인포</title>
<meta name="description" content="{a['desc']}">
<meta property="og:type" content="article">
<meta property="og:title" content="{a['title']}">
<meta property="og:description" content="{a['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="주호15 인포">
<meta property="og:locale" content="ko_KR">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">{ld}</script>
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
<a href="/">홈</a> › {a['title']}
</nav>

<article class="article-content">
{a['intro']}
{ad('2318766489', 'in-article')}
{a['rest']}
<div class="official-links">
<h2>공식 확인 링크</h2>
<ul>
{official}
</ul>
<p>신청 요건과 지원금액은 매년 변경될 수 있으므로 반드시 공식 사이트에서 최신 정보를 확인하세요.</p>
</div>
</article>

{ad('8085568257', 'in-article')}

<section class="related-articles">
<h2>함께 보면 좋은 글</h2>
<ul>
{related}
</ul>
</section>

<div class="notice">
<strong>안내:</strong> 본 글은 이해를 돕기 위한 일반 정보이며, 법률·행정 해석을 대체하지 않습니다. 실제 신청 가능 여부와 지원금액은 관할 기관의 최신 안내를 확인하시기 바랍니다.
</div>

<p class="update-date">최종 업데이트: {UPDATE}</p>

{ad('2318766489')}

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


HUB_LINKS = {
"near-poor-benefits.html": [("차상위계층 신청 방법", "/near-poor-application.html")],
"basic-livelihood.html": [("기초수급 vs 차상위 차이", "/basic-livelihood-vs-near-poor.html")],
"housing-benefit.html": [("주거급여 탈락 이유", "/housing-benefit-rejection.html")],
"child-tax-credit.html": [("자녀장려금 2026 일정", "/child-tax-2026.html")],
"longterm-care.html": [("장기요양 등급 변경", "/longterm-care-grade-change.html")],
"medical-checkup.html": [("건강검진 놓쳤을 때", "/medical-checkup-missed.html")],
"retirement-pension.html": [("퇴직연금 중도인출", "/retirement-pension-withdrawal.html")],
"telecom-discount.html": [("통신비 감면 필요 서류", "/telecom-discount-documents.html")],
"national-pension.html": [("국민연금 공백·추후납부", "/national-pension-gap.html")],
"earned-income-credit.html": [("근로장려금 환수 대처", "/earned-income-repayment.html")],
}


def patch_related(filename, new_items):
    path = ROOT / filename
    if not path.exists():
        return
    html = path.read_text(encoding="utf-8")
    m = re.search(
        r'(<section class="related-articles">\s*<h2>함께 보면 좋은 글</h2>\s*<ul>)(.*?)(</ul>)',
        html,
        re.S,
    )
    if not m:
        return
    existing = m.group(2)
    for title, href in new_items:
        if href in existing:
            continue
        existing = f'\n<li><a href="{href}">{title}</a></li>' + existing
    html = html[: m.start(2)] + existing + html[m.end(2) :]
    path.write_text(html, encoding="utf-8")
    print(f"hub-related: {filename}")


def main():
    for a in ARTICLES:
        (ROOT / a["file"]).write_text(build_page(a), encoding="utf-8")
        print(f"created: {a['file']}")
    for fname, links in HUB_LINKS.items():
        patch_related(fname, links)


if __name__ == "__main__":
    main()
