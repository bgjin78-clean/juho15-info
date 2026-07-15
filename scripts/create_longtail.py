#!/usr/bin/env python3
"""Create long-tail / situation-guide articles and update hub links."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.juho15.com"
UPDATE = "2026년 7월 15일"
UPDATE_ISO = "2026-07-15"
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
"file": "basic-pension-rejection.html",
"title": "기초연금 탈락 이유와 재신청 방법",
"desc": "기초연금 탈락 사유, 소득인정액·재산 문제, 배우자 소득, 재산 처분 후 재신청 체크리스트를 정리했습니다.",
"related": [
("기초연금 수급자격과 신청방법", "/basic-pension.html"),
("부부 기초연금 신청 시 확인할 점", "/basic-pension-couple.html"),
("국민연금 예상수령액 조회", "/national-pension.html"),
("노인일자리와 기초연금", "/senior-job-basic-pension.html"),
],
"official": [
("국민연금공단 기초연금", "https://www.nps.or.kr"),
("복지로", "https://www.bokjiro.go.kr"),
],
"intro": """<h1>기초연금 탈락 이유와 재신청 방법</h1>
<p>기초연금을 신청했다가 탈락하면 “나이만 되면 되는데”라고 낙담하기 쉽습니다. 실제로는 <strong>소득인정액</strong>이 선정기준을 넘었거나, <strong>배우자·자녀 재산</strong>이 함께 반영된 경우가 많습니다. 탈락 고지서를 기준으로 원인을 확인하고, 상황이 바뀌면 재신청할 수 있습니다.</p>
""",
"rest": """<h2>탈락이 자주 나는 이유</h2>
<ul>
<li><strong>소득인정액 초과</strong> — 근로·연금·임대소득 + 재산의 소득환산액 합계가 기준 초과</li>
<li><strong>배우자 소득·재산</strong> — 부부가구로 심사되어 단독보다 기준이 다르게 적용</li>
<li><strong>금융재산·부동산</strong> — 실제 생활비와 별개로 예금·집·토지가 크게 반영</li>
<li><strong>자동차</strong> — 고가·다차량은 재산에 반영될 수 있음</li>
<li><strong>주소·국적·거주</strong> — 해외 장기 체류 등 거주 요건 미충족</li>
</ul>
<h2>탈락 고지서에서 볼 것</h2>
<ol>
<li>통보문의 <strong>탈락 사유</strong> (소득인정액, 재산 등)</li>
<li>본인·배우자의 <strong>소득평가액·재산의 소득환산액</strong></li>
<li>선정기준액과의 차이(얼마를 넘었는지)</li>
</ol>
<p>금액 차이가 크지 않으면, 연금 수령액 변동·재산 처분·가구원 변경 후 재도전이 가능한 경우가 있습니다.</p>
<h2>재신청 전 체크리스트</h2>
<ul>
<li>배우자와 사별·이혼·별거로 가구 형태가 바뀌었는가</li>
<li>예금·보험·주식 등 금융재산을 줄였는가</li>
<li>부동산 매도·명의 이전으로 재산이 줄었는가</li>
<li>국민연금·이자 등 월 소득이 줄었는가</li>
<li>만 65세 도래 직후 첫 신청이 너무 이르게 처리됐는가</li>
</ul>
<h2>재신청 방법</h2>
<ol>
<li>주소지 행정복지센터 또는 국민연금공단 지사 방문</li>
<li>복지로에서 온라인 신청(가능한 경우)</li>
<li>소득·재산이 바뀐 시점의 서류를 함께 제출</li>
</ol>
<p>신청한 달부터 심사가 시작되므로, 기준에 가까워졌다면 미루지 않는 것이 유리합니다.</p>
<h2>자주 묻는 질문</h2>
<h3>탈락하면 영원히 못 받나요?</h3>
<p>아닙니다. 소득·재산·가구 상황이 바뀌면 다시 받을 수 있습니다.</p>
<h3>국민연금을 많이 받으면 무조건 탈락인가요?</h3>
<p>국민연금만으로 결정되지 않습니다. 전체 소득인정액 기준으로 판단합니다.</p>
<h3>이의신청은 가능한가요?</h3>
<p>통보 내용이 사실과 다르다고 판단되면 관할 기관에 이의·정정 요청을 할 수 있습니다.</p>
""",
},
{
"file": "basic-pension-couple.html",
"title": "부부 기초연금 신청 시 확인할 점",
"desc": "부부 기초연금 소득인정액, 한 명만 받는 경우, 감액, 배우자 동의·서류, 동시 신청 요령을 정리했습니다.",
"related": [
("기초연금 수급자격과 신청방법", "/basic-pension.html"),
("기초연금 탈락 이유와 재신청", "/basic-pension-rejection.html"),
("국민연금 조기수령과 연기수령", "/national-pension-early.html"),
("노인일자리 신청방법", "/senior-job.html"),
],
"official": [
("국민연금공단 기초연금", "https://www.nps.or.kr"),
("복지로", "https://www.bokjiro.go.kr"),
],
"intro": """<h1>부부 기초연금 신청 시 확인할 점</h1>
<p>배우자가 있으면 기초연금은 <strong>부부가구 선정기준</strong>으로 심사됩니다. 혼자 신청해도 배우자 소득·재산이 함께 반영되고, 둘 다 받으면 지급액이 일부 조정되는 경우가 있습니다. 신청 전에 “한 명만 받을지, 둘 다 받을지”를 기준으로 확인하세요.</p>
""",
"rest": """<h2>부부 심사의 핵심</h2>
<ul>
<li>소득인정액은 <strong>부부 합산</strong>으로 계산</li>
<li>부부가구 선정기준액은 단독가구보다 높게 설정(연도별 고시)</li>
<li>부부 모두 수급 시 <strong>감액(부부감액)</strong>이 적용될 수 있음</li>
</ul>
<h2>한 명만 받는 경우</h2>
<p>배우자 중 한 명만 만 65세에 도달했거나, 한 명만 요건을 충족하면 그 사람만 수급할 수 있습니다. 이후 배우자가 65세가 되면 추가 신청이 필요합니다.</p>
<h2>둘 다 신청할 때</h2>
<ol>
<li>각자 또는 대리로 신청 가능(서류는 배우자 동의 필요할 수 있음)</li>
<li>배우자 <strong>금융정보 제공 동의서</strong> 준비</li>
<li>공통 재산·임대차 계약서는 한 부만 제출해도 되는 경우가 많음</li>
</ol>
<h2>부부감액이 궁금할 때</h2>
<p>부부 모두 기초연금을 받으면 단독 최대액보다 1인당 지급액이 줄어들 수 있습니다. “둘 다 받는 것이 유리한지”는 소득인정액과 감액 후 합계로 비교하는 것이 좋습니다. 정확한 예상액은 공단·복지센터 상담이 안전합니다.</p>
<h2>자주 하는 실수</h2>
<ul>
<li>배우자 통장·예금을 누락하고 신고</li>
<li>별거 중인데 부부가구로 묶이는지 확인하지 않음</li>
<li>이혼·재혼 후 가구원 정보를 갱신하지 않음</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>배우자가 고소득이면 나는 탈락인가요?</h3>
<p>부부 합산 소득인정액이 기준을 넘으면 둘 다 탈락할 수 있습니다.</p>
<h3>배우자 명의 집도 포함되나요?</h3>
<p>원칙적으로 부부 소유 재산은 함께 반영됩니다.</p>
""",
},
{
"file": "national-pension-early.html",
"title": "국민연금 조기수령과 연기수령 비교",
"desc": "국민연금 조기수령·연기수령 장단점, 감액·가산율, 기초연금과의 관계, 선택 기준을 정리했습니다.",
"related": [
("국민연금 예상수령액 조회", "/national-pension.html"),
("기초연금 수급자격과 신청방법", "/basic-pension.html"),
("부부 기초연금 신청 시 확인할 점", "/basic-pension-couple.html"),
("퇴직연금 조회방법", "/retirement-pension.html"),
],
"official": [
("국민연금공단", "https://www.nps.or.kr"),
],
"intro": """<h1>국민연금 조기수령과 연기수령 비교</h1>
<p>국민연금은 법정 수령 연령을 기준으로 <strong>최대 5년 조기</strong> 또는 <strong>최대 5년 연기</strong>해 받을 수 있습니다. 빨리 받으면 매월 액이 줄고, 늦게 받으면 매월 액이 늘어납니다. 건강·생활비·기대수명·기초연금을 함께 보고 고르는 것이 중요합니다.</p>
""",
"rest": """<h2>조기수령이란?</h2>
<p>수령 개시 연령보다 최대 5년 앞당겨 받는 방식입니다. 매월 연금액이 <strong>일정 비율 감액</strong>되며, 한 번 조기 수령을 시작하면 원칙적으로 되돌리기 어렵습니다.</p>
<h2>연기수령이란?</h2>
<p>수령을 미루면 미룬 기간만큼 월 연금액이 <strong>가산</strong>됩니다. 생활비가 충분하고, 더 오래 받을 가능성이 있다고 판단될 때 검토합니다.</p>
<h2>선택을 가르는 기준</h2>
<ul>
<li><strong>당장 생활비</strong>가 부족한가 → 조기 수령 검토</li>
<li><strong>다른 소득·저축</strong>이 충분한가 → 연기 수령 검토</li>
<li><strong>건강·가족력</strong>상 수령 기간이 짧을 수 있는가</li>
<li><strong>기초연금</strong> 소득인정액에 국민연금이 미치는 영향</li>
</ul>
<h2>기초연금과의 관계</h2>
<p>국민연금을 빨리·많이 받으면 기초연금 소득인정액에 반영되어 기초연금이 줄거나 탈락할 수 있습니다. 반대로 연기해 당장은 국민연금을 받지 않으면 기초연금 심사에 유리한 경우도 있습니다. <strong>두 제도를 합친 총액</strong>으로 비교하세요.</p>
<h2>신청 전 확인</h2>
<ol>
<li>공단 앱·홈페이지에서 조기·연기 시 예상액 비교</li>
<li>수령 개시 연령(출생연도별) 확인</li>
<li>배우자 유족연금·분할연금 등 가족 상황 점검</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>조기수령 후 마음이 바뀌면?</h3>
<p>개시 후에는 취소가 제한적입니다. 신중히 결정하세요.</p>
<h3>연기만 하면 무조건 유리한가요?</h3>
<p>아닙니다. 수령 기간이 짧으면 총액이 줄어들 수 있습니다.</p>
""",
},
{
"file": "senior-job-basic-pension.html",
"title": "노인일자리와 기초연금 동시 가능 여부",
"desc": "노인일자리 활동비가 기초연금에 미치는 영향, 공익활동형 참여 시 주의점, 중복 가능 여부를 정리했습니다.",
"related": [
("노인일자리 신청방법", "/senior-job.html"),
("기초연금 수급자격과 신청방법", "/basic-pension.html"),
("기초연금 탈락 이유와 재신청", "/basic-pension-rejection.html"),
("장기요양보험 등급 신청방법", "/longterm-care.html"),
],
"official": [
("노인일자리 여기", "https://www.seniorro.or.kr"),
("국민연금공단 기초연금", "https://www.nps.or.kr"),
],
"intro": """<h1>노인일자리와 기초연금 동시 가능 여부</h1>
<p>“기초연금을 받으면 노인일자리를 못 한다”, “일자리를 하면 기초연금이 끊긴다”는 이야기가 많습니다. 실제로는 <strong>사업 유형</strong>과 <strong>활동비의 소득 반영 방식</strong>에 따라 다릅니다. 대부분 공익활동형은 기초연금 수급자를 우선 모집하지만, 활동비가 소득인정액에 어떻게 잡히는지는 미리 확인해야 합니다.</p>
""",
"rest": """<h2>기본 정리</h2>
<ul>
<li>공익활동형 노인일자리는 <strong>기초연금 수급자 우선</strong>인 경우가 많음</li>
<li>활동비는 “월급”과 성격이 다르게 설계된 사업이 많음</li>
<li>다만 지자체·사업단마다 <strong>소득 반영 규칙</strong>이 다를 수 있음</li>
</ul>
<h2>기초연금에 영향이 생길 수 있는 경우</h2>
<ol>
<li>시장형·취업알선형 등 <strong>근로소득</strong>에 가까운 수입</li>
<li>활동비가 커져 가구 소득인정액이 선정기준을 넘음</li>
<li>다른 근로·사업소득과 합산되어 초과</li>
</ol>
<h2>신청 전에 확인할 질문</h2>
<ul>
<li>이 사업 활동비가 기초연금 소득인정액에 포함되나요?</li>
<li>월 활동 시간과 최대 활동비는 얼마인가요?</li>
<li>기초연금 수급 중 참가 제한이 있나요?</li>
</ul>
<p>주민센터·노인복지관·사업 담당자에게 위 질문을 그대로 확인해 두는 것이 안전합니다.</p>
<h2>실무 팁</h2>
<ul>
<li>기초연금 통지서의 소득인정액과 선정기준 여유분을 먼저 파악</li>
<li>여유분이 작으면 활동 시간이 짧은 유형을 검토</li>
<li>중도 이탈·재신청 규칙을 모집 공고에서 확인</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>기초연금 받으면 무조건 참여 가능한가요?</h3>
<p>공익활동형은 우선 대상인 경우가 많지만, 모집 인원·지역 배정에 따라 탈락할 수 있습니다.</p>
<h3>일자리 하면 기초연금이 바로 끊기나요?</h3>
<p>일반적으로 즉시 중단되지는 않습니다. 문제는 다음 소득조사·변동신고 시 반영 여부입니다.</p>
""",
},
{
"file": "earned-income-2026.html",
"title": "근로장려금 2026 신청기간과 일정",
"desc": "근로장려금 2026 정기·반기 신청기간, 지급 시기, 놓치지 않는 체크 포인트를 정리했습니다.",
"related": [
("근로장려금 신청방법 총정리", "/earned-income-credit.html"),
("근로장려금 안내문 없이 신청", "/earned-income-no-letter.html"),
("자녀장려금 신청자격", "/child-tax-credit.html"),
("연말정산 환급금 조회", "/year-end-tax-refund.html"),
],
"official": [
("국세청 홈택스", "https://www.hometax.go.kr"),
],
"intro": """<h1>근로장려금 2026 신청기간과 일정</h1>
<p>근로장려금은 매해 <strong>정기신청</strong>과 <strong>반기신청</strong> 일정이 정해져 있습니다. 2026년에도 대체로 상반기·하반기 패턴을 따르지만, <strong>정확한 시작·마감일은 국세청 공고</strong>가 기준입니다. 아래는 일정을 놓치지 않기 위한 실무 가이드입니다.</p>
""",
"rest": """<h2>신청 유형별 구분</h2>
<table>
<tr><th>유형</th><th>대상 소득</th><th>대략적 시기(참고)</th></tr>
<tr><td>정기신청</td><td>전년도 소득</td><td>보통 3월~5월</td></tr>
<tr><td>상반기 반기</td><td>당해 상반기 근로소득</td><td>보통 3월~5월</td></tr>
<tr><td>하반기 반기</td><td>당해 하반기 근로소득</td><td>보통 9월~11월</td></tr>
</table>
<p>사업소득·종교인 소득은 반기 대상이 아닐 수 있습니다. 본인 소득 종류를 먼저 확인하세요.</p>
<h2>2026년 일정 확인법</h2>
<ol>
<li>국세청·홈택스 공지에서 “근로·자녀장려금” 검색</li>
<li>안내문 SMS·우편에 적힌 신청 기한 확인</li>
<li>손택스 앱 배너/알림으로 마감일 체크</li>
</ol>
<h2>놓치기 쉬운 포인트</h2>
<ul>
<li>마감일 당일 밤 자정 기준 혼동</li>
<li>안내문을 못 받아 신청 자체를 포기</li>
<li>반기 신청 후 정기 정산 일정 미확인</li>
</ul>
<h2>지급은 언제?</h2>
<p>정기신청은 보통 신청 해 9월 전후, 반기는 신청 차수에 따라 연말 또는 이듬해 초에 지급되는 경우가 많습니다. 정확한 지급일은 매년 공지를 따릅니다.</p>
<h2>자주 묻는 질문</h2>
<h3>기한을 하루 놓치면?</h3>
<p>정기 기한을 지나면 추가 기한이 없는 경우가 많습니다. 가능하면 마감 며칠 전 미리 신청하세요.</p>
<h3>2025년 소득 기준인가요, 2026년인가요?</h3>
<p>정기신청은 보통 <strong>직전 연도 소득</strong>을 기준으로 합니다.</p>
""",
},
{
"file": "earned-income-no-letter.html",
"title": "근로장려금 안내문 없이 신청하는 방법",
"desc": "근로장려금 안내문을 못 받았을 때 홈택스·손택스에서 대상 조회 후 직접 신청하는 방법을 정리했습니다.",
"related": [
("근로장려금 신청방법 총정리", "/earned-income-credit.html"),
("근로장려금 2026 신청기간", "/earned-income-2026.html"),
("자녀장려금 신청자격", "/child-tax-credit.html"),
("고용보험 가입이력 조회", "/employment-insurance.html"),
],
"official": [
("국세청 홈택스", "https://www.hometax.go.kr"),
],
"intro": """<h1>근로장려금 안내문 없이 신청하는 방법</h1>
<p>안내 문자·우편을 받지 못했다고 무조건 대상이 아닌 것은 아닙니다. <strong>요건만 충족하면 홈택스에서 직접 조회·신청</strong>할 수 있습니다. 안내문은 “신청을 쉽게 해 주는 초대장”에 가깝습니다.</p>
""",
"rest": """<h2>안내문이 없어도 되는 이유</h2>
<p>국세청이 파악한 소득·가구 정보로 안내 대상을 추리지만, 누락되거나 최근 가구 변동이 반영되지 않을 수 있습니다. 본인이 요건을 충족한다고 판단되면 직접 신청하는 편이 안전합니다.</p>
<h2>홈택스 직접 신청 순서</h2>
<ol>
<li>홈택스 또는 손택스 로그인</li>
<li>근로·자녀장려금 → <strong>신청하기</strong> / 정기·반기 선택</li>
<li>본인인증 후 가구원·소득·재산 정보 확인</li>
<li>환급 계좌 입력 후 제출</li>
</ol>
<h2>신청 전 준비물</h2>
<ul>
<li>공동인증서·간편인증</li>
<li>배우자·부양가족 정보</li>
<li>본인 명의 계좌</li>
<li>임대·예금 등 재산 개요(대략이라도)</li>
</ul>
<h2>대상이 안 나온다면</h2>
<ul>
<li>소득·재산 기준 초과 가능성</li>
<li>가구 유형 오분류(단독/홑벌이/맞벌이)</li>
<li>신청 기간이 아님</li>
</ul>
<p>그래도 의심되면 장려금 상담센터 또는 세무서에 “비안내자 신청” 가능 여부를 문의하세요.</p>
<h2>자주 묻는 질문</h2>
<h3>안내문이 있어야 개별인증번호가 있나요?</h3>
<p>안내문이 있으면 간편합니다. 없어도 로그인 후 본인인증으로 신청 가능한 경우가 많습니다.</p>
<h3>작년에 받았는데 올해 안내가 없어요</h3>
<p>소득·재산·가구가 바뀌면 안내 대상에서 빠질 수 있습니다. 직접 조회로 확인하세요.</p>
""",
},
{
"file": "health-refund-scam.html",
"title": "건강보험 환급금 사칭 문자·전화 구별법",
"desc": "건강보험 환급금 사기 문자·카톡·전화 특징, 공식 조회 방법, 안전한 대처 요령을 정리했습니다.",
"related": [
("건강보험 환급금 조회방법", "/health-insurance-refund.html"),
("건강보험료 계산방법", "/health-insurance-premium.html"),
("연말정산 환급금 조회", "/year-end-tax-refund.html"),
("실손보험 청구방법", "/insurance-claim.html"),
],
"official": [
("국민건강보험공단", "https://www.nhis.or.kr"),
("금융감독원", "https://www.fss.or.kr"),
],
"intro": """<h1>건강보험 환급금 사칭 문자·전화 구별법</h1>
<p>“고객님 미환급금이 있습니다. 링크에서 신청하세요”라는 문자·카톡이 자주 옵니다. 실제 환급금이 있을 수 있지만, <strong>링크를 누르거나 계좌·인증번호를 넘기면</strong> 스미싱·보이스피싱으로 이어질 수 있습니다. 공식 경로만 사용하세요.</p>
""",
"rest": """<h2>사기 문자의 흔한 특징</h2>
<ul>
<li>단축 URL, 낯선 도메인, “즉시 소멸” 압박</li>
<li>카카오톡·문자로 <strong>개인정보·계좌·OTP</strong> 요구</li>
<li>“환급 수수료”를 먼저 입금하라고 함</li>
<li>발신번호가 공단·정부처럼 보이지만 실제로는 변작</li>
</ul>
<h2>안전한 확인 방법</h2>
<ol>
<li>문자 링크를 누르지 않음</li>
<li><strong>The건강보험</strong> 앱 또는 nhis.or.kr에 직접 접속</li>
<li>본인인증 후 환급금·추가납부 조회</li>
<li>필요 시 공단 고객센터(1577-1000)로 전화(문자 번호 재다이얼 금지)</li>
</ol>
<h2>진짜 환급이 있을 때</h2>
<p>공단 앱에서 금액이 보이면 본인 명의 계좌를 등록해 신청합니다. 공단은 <strong>계좌 비밀번호·OTP·보안카드를 요구하지 않습니다.</strong></p>
<h2>피해를 입었다면</h2>
<ul>
<li>즉시 금융사에 계좌 지급정지 요청</li>
<li>경찰·금융감독원·전자금융사기 신고</li>
<li>공단에는 공식 채널로만 상담</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>공단에서 문자를 보내기도 하나요?</h3>
<p>안내 문자가 있을 수 있으나, 신청은 반드시 공식 앱·홈페이지에서 하세요.</p>
<h3>가족 명의 환급을 대신 찾아달라는 전화는?</h3>
<p>대부분 사기입니다. 본인 인증 없이 대리로 찾아준다는 말은 경계하세요.</p>
""",
},
{
"file": "unemployment-voluntary.html",
"title": "자발적 퇴사 시 실업급여 가능 여부",
"desc": "자진 퇴사해도 실업급여가 되는 예외 사유, 권고사직과의 차이, 증빙 서류와 신청 팁을 정리했습니다.",
"related": [
("실업급여 신청조건과 신청방법", "/unemployment-benefit.html"),
("고용보험 가입이력 조회", "/employment-insurance.html"),
("근로장려금 신청방법", "/earned-income-credit.html"),
("연말정산 환급금 조회", "/year-end-tax-refund.html"),
],
"official": [
("고용24", "https://www.work24.go.kr"),
],
"intro": """<h1>자발적 퇴사 시 실업급여 가능 여부</h1>
<p>원칙적으로 <strong>스스로 사표를 쓰면</strong> 실업급여(구직급여)가 어렵습니다. 다만 법이 정한 <strong>정당한 이직 사유</strong>가 있으면 자진 퇴사로 보여도 수급이 인정될 수 있습니다. 핵심은 “그만둔 이유”를 서류로 남기는 것입니다.</p>
""",
"rest": """<h2>원칙</h2>
<ul>
<li>개인 사유·이직·창업 목적의 단순 자진 퇴사 → 불승인 가능성 큼</li>
<li>권고사직·계약만료·해고 등 비자발적 이직 → 심사 대상</li>
<li>자진 퇴사처럼 보여도 <strong>불가피한 사유</strong>면 예외 검토</li>
</ul>
<h2>예외로 검토되는 대표 사유(요약)</h2>
<ul>
<li>임금 체불, 최저임금 미달, 근로조건 현저한 저하</li>
<li>괴롭힘·성희롱 등 사업장 내 문제</li>
<li>통근 곤란(원거리 전근 등)으로 근로 지속 곤란</li>
<li>질병·부상으로 업무 수행이 어렵고 휴직 등이 여의치 않음</li>
<li>부모·자녀 돌봄 등 법이 정한 가족 돌봄 사유</li>
</ul>
<p>세부 인정 기준은 고용센터 심사에 따라 달라지므로, 해당 사유가 있으면 <strong>증빙을 먼저 모으고</strong> 상담받으세요.</p>
<h2>준비하면 유리한 증빙</h2>
<ul>
<li>급여명세서, 체불 내역, 근로계약서</li>
<li>병원 진단서·소견서</li>
<li>사직서에 적힌 퇴사 사유(가능하면 구체적)</li>
<li>회사 통보 문자·메일, 고충 처리 기록</li>
</ul>
<h2>신청 팁</h2>
<ol>
<li>이직확인서의 이직 사유 코드를 반드시 확인</li>
<li>회사 기재가 사실과 다르면 고용센터에 이의 제기</li>
<li>퇴사 후 늦지 않게(원칙 12개월 이내) 신청</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>권고사직이면 무조건 되나요?</h3>
<p>가능성 높지만, 이직확인서·면담 기록이 중요합니다.</p>
<h3>사직서에 “개인 사정”만 적었어요</h3>
<p>심사에서 불리할 수 있습니다. 실제 사유 증빙을 보강하세요.</p>
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


def patch_related(filename, new_items):
    path = ROOT / filename
    if not path.exists():
        return
    html = path.read_text(encoding="utf-8")
    m = re.search(r'(<section class="related-articles">\s*<h2>함께 보면 좋은 글</h2>\s*<ul>)(.*?)(</ul>)', html, re.S)
    if not m:
        return
    existing = m.group(2)
    for title, href in new_items:
        if href in existing:
            continue
        existing = f'\n<li><a href="{href}">{title}</a></li>' + existing
    html = html[:m.start(2)] + existing + html[m.end(2):]
    path.write_text(html, encoding="utf-8")
    print(f"hub-related: {filename}")


def main():
    for a in ARTICLES:
        path = ROOT / a["file"]
        path.write_text(build_page(a), encoding="utf-8")
        print(f"created: {a['file']}")

    patch_related("basic-pension.html", [
        ("기초연금 탈락 이유와 재신청", "/basic-pension-rejection.html"),
        ("부부 기초연금 신청 시 확인할 점", "/basic-pension-couple.html"),
        ("노인일자리와 기초연금", "/senior-job-basic-pension.html"),
    ])
    patch_related("national-pension.html", [
        ("국민연금 조기수령과 연기수령 비교", "/national-pension-early.html"),
        ("기초연금 탈락 이유와 재신청", "/basic-pension-rejection.html"),
    ])
    patch_related("earned-income-credit.html", [
        ("근로장려금 2026 신청기간과 일정", "/earned-income-2026.html"),
        ("근로장려금 안내문 없이 신청", "/earned-income-no-letter.html"),
    ])
    patch_related("health-insurance-refund.html", [
        ("건강보험 환급금 사칭 문자 구별법", "/health-refund-scam.html"),
    ])
    patch_related("unemployment-benefit.html", [
        ("자발적 퇴사 시 실업급여 가능 여부", "/unemployment-voluntary.html"),
    ])
    patch_related("senior-job.html", [
        ("노인일자리와 기초연금 동시 가능 여부", "/senior-job-basic-pension.html"),
    ])


if __name__ == "__main__":
    main()
