#!/usr/bin/env python3
"""Batch 2: more long-tail / situation-guide articles."""
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
"file": "basic-pension-income.html",
"title": "기초연금 소득인정액 계산 쉽게 보기",
"desc": "기초연금 소득인정액 구성(소득평가액·재산의 소득환산), 단독·부부가구 차이, 줄일 수 있는 요인을 쉽게 정리했습니다.",
"related": [
("기초연금 수급자격과 신청방법", "/basic-pension.html"),
("기초연금 탈락 이유와 재신청", "/basic-pension-rejection.html"),
("부부 기초연금 신청 시 확인할 점", "/basic-pension-couple.html"),
("국민연금 조기수령과 연기수령", "/national-pension-early.html"),
],
"official": [
("국민연금공단 기초연금", "https://www.nps.or.kr"),
("복지로", "https://www.bokjiro.go.kr"),
],
"intro": """<h1>기초연금 소득인정액 계산 쉽게 보기</h1>
<p>기초연금 통과 여부는 월급이 아니라 <strong>소득인정액</strong>으로 결정됩니다. 현금 소득뿐 아니라 예금·집·자동차까지 “소득처럼” 환산해 합산하기 때문에, 생활이 빠듯해도 탈락하는 경우가 생깁니다. 구성을 알면 탈락·재신청 판단이 쉬워집니다.</p>
""",
"rest": """<h2>소득인정액 = 소득평가액 + 재산의 소득환산액</h2>
<ul>
<li><strong>소득평가액</strong> — 근로·사업·재산소득, 공적이전소득(국민연금 등)을 월 단위로 환산한 값</li>
<li><strong>재산의 소득환산액</strong> — 금융재산·부동산 등에서 기본재산액·부채를 반영한 뒤, 일정 요율로 월 소득처럼 환산한 값</li>
</ul>
<p>두 값을 더해 단독·부부가구 <strong>선정기준액</strong>과 비교합니다. 기준액은 매년 고시됩니다.</p>
<h2>소득평가액에서 자주 나오는 항목</h2>
<ul>
<li>근로소득(일부 공제 후 반영되는 경우 있음)</li>
<li>사업·임대소득</li>
<li>국민연금·특수직역연금 등 공적이전소득</li>
<li>이자·배당 등 재산소득</li>
</ul>
<h2>재산의 소득환산에서 보는 것</h2>
<ul>
<li>일반재산: 주택, 토지, 건축물 등</li>
<li>금융재산: 예금, 적금, 보험, 주식 등</li>
<li>자동차(기준에 따라 재산 반영)</li>
<li>부채(전세보증금 대출 등)는 일부 차감될 수 있음</li>
<li>기본재산액(지역·가구 유형별 공제) 적용</li>
</ul>
<h2>혼자서 대략 감 잡는 방법</h2>
<ol>
<li>월 들어오는 공적연금·이자·임대료를 합산</li>
<li>예금·보험 해약환급금 등 금융재산 합계를 적어 둠</li>
<li>시세·공시지가 기준 집·토지 가액과 대출 잔액을 확인</li>
<li>복지센터·공단에 “소득인정액 모의계산” 상담 요청</li>
</ol>
<p>정확한 금액은 전산 연계·공제율이 달라 직접 계산과 오차가 날 수 있습니다. 최종은 관할 기관 통보가 기준입니다.</p>
<h2>인정액을 낮추려면(일반적)</h2>
<ul>
<li>불필요한 고액 예금·보험을 정리(단, 성급한 증여·명의이전은 주의)</li>
<li>부채·임대차 계약을 빠짐없이 신고</li>
<li>배우자 소득·재산이 합산되는 부부가구 구조 확인</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>국민연금만 받으면 무조건 탈락인가요?</h3>
<p>아닙니다. 국민연금은 소득평가액에 들어가지만, 다른 소득·재산이 적으면 기준 이하일 수 있습니다.</p>
<h3>자식 명의 집도 잡히나요?</h3>
<p>본인·배우자 소유가 아니면 원칙적으로 본인 재산이 아닙니다. 다만 거주·사용 관계에 따라 확인이 필요할 수 있습니다.</p>
""",
},
{
"file": "earned-income-household.html",
"title": "근로장려금 단독·홑벌이·맞벌이 소득 기준",
"desc": "근로장려금 가구 유형(단독·홑벌이·맞벌이)별 소득·재산 기준 차이, 본인 유형 판별법, 신청 전 확인점을 정리했습니다.",
"related": [
("근로장려금 신청방법 총정리", "/earned-income-credit.html"),
("근로장려금 2026 신청기간", "/earned-income-2026.html"),
("근로장려금 안내문 없이 신청", "/earned-income-no-letter.html"),
("자녀장려금 신청자격", "/child-tax-credit.html"),
],
"official": [
("국세청 홈택스", "https://www.hometax.go.kr"),
],
"intro": """<h1>근로장려금 단독·홑벌이·맞벌이 소득 기준</h1>
<p>근로장려금은 “가구 유형”에 따라 <strong>소득 상한</strong>과 <strong>지급액 구간</strong>이 달라집니다. 혼자 사는지, 배우자가 있는지, 맞벌이인지에 따라 같은 소득이라도 대상 여부가 갈립니다. 신청 전에 본인 유형부터 확정하세요.</p>
""",
"rest": """<h2>가구 유형 한눈에</h2>
<table>
<tr><th>유형</th><th>대략적 의미</th></tr>
<tr><td>단독가구</td><td>배우자·부양자녀·부양부모가 없는 가구</td></tr>
<tr><td>홑벌이 가구</td><td>배우자가 있으나 맞벌이 요건 미충족, 또는 부양자녀·70세 이상 부모 등</td></tr>
<tr><td>맞벌이 가구</td><td>배우자와 본인의 총급여 등이 일정 금액 이상인 맞벌이</td></tr>
</table>
<p>세부 요건(부양자녀 나이, 배우자 총급여 기준 등)은 연도별 국세청 안내를 따릅니다.</p>
<h2>소득 기준이 중요한 이유</h2>
<ul>
<li>유형마다 <strong>총소득 상한</strong>이 다름(단독 &lt; 홑벌이 &lt; 맞벌이인 경우가 일반적)</li>
<li>상한을 넘으면 장려금 대상에서 제외</li>
<li>상한 안이어도 소득 구간에 따라 지급액이 달라짐</li>
</ul>
<h2>재산 기준도 같이 본다</h2>
<p>가구원 합산 재산이 일정 기준을 넘으면 지급이 제한되거나 제외될 수 있습니다. 주택·예금·자동차 등을 본인만 기준으로 보면 오판하기 쉽습니다.</p>
<h2>유형을 잘못 고르는 실수</h2>
<ul>
<li>별거 중인데 배우자 정보를 누락</li>
<li>아르바이트 배우자 소득을 빠져먹음</li>
<li>자녀가 성인이어도 부양 요건을 착각</li>
</ul>
<h2>확인 순서</h2>
<ol>
<li>홈택스에서 가구원·유형 자동 판정 화면 확인</li>
<li>전년도(또는 반기) 총소득·배우자 총급여 점검</li>
<li>재산 합산 가능성이 있으면 대략 가액 정리</li>
<li>안내문 없이도 직접 신청·모의계산 가능</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>맞벌이면 불리한가요?</h3>
<p>소득 상한이 더 높은 편이라 유리할 수도 있습니다. 다만 합산 소득이 커지면 구간이 불리해질 수 있습니다.</p>
<h3>자녀장려금은 유형이 같나요?</h3>
<p>자녀장려금은 별도 제도이며 부양자녀 요건이 핵심입니다. 근로장려금과 동시 신청이 가능한 경우가 많습니다.</p>
""",
},
{
"file": "health-copay-cap.html",
"title": "본인부담상한제 환급 시기와 조회 방법",
"desc": "건강보험 본인부담상한제란 무엇인지, 환급 시기, 소득분위별 상한, 앱에서 조회·신청하는 방법을 정리했습니다.",
"related": [
("건강보험 환급금 조회방법", "/health-insurance-refund.html"),
("건강보험 환급금 사칭 구별법", "/health-refund-scam.html"),
("건강보험료 계산방법", "/health-insurance-premium.html"),
("실손보험 청구방법", "/insurance-claim.html"),
],
"official": [
("국민건강보험공단", "https://www.nhis.or.kr"),
],
"intro": """<h1>본인부담상한제 환급 시기와 조회 방법</h1>
<p>병원비를 많이 쓴 해에는 <strong>본인부담상한제</strong>로 초과분을 돌려받을 수 있습니다. 일반 “보험료 환급”과 달리, 의료비 본인부담이 소득 구간별 상한을 넘었을 때 적용됩니다. 시기와 조회 경로를 알면 사기 문자에도 덜 당합니다.</p>
""",
"rest": """<h2>본인부담상한제란?</h2>
<p>가입자·피부양자가 1년 동안 부담한 의료비(본인부담금)가 소득 수준에 따른 <strong>상한액</strong>을 초과하면, 초과분을 공단이 부담·환급하는 제도입니다. 비급여·선별급여 등은 제외되는 항목이 있으니 영수증만으로 단정하지 마세요.</p>
<h2>환급은 언제 들어오나</h2>
<ul>
<li><strong>사전급여</strong> — 동일 요양기관에서 상한을 넘긴 경우, 병원 창구에서 본인부담을 제한하는 방식</li>
<li><strong>사후정산(환급)</strong> — 여러 병원을 이용했거나 연말에 합산해 초과분이 확정되면, 이듬해 안내·환급</li>
</ul>
<p>사후정산은 보통 <strong>다음 해 상반기~중반</strong>에 안내되는 경우가 많습니다. 정확한 일정은 공단 공지를 확인하세요.</p>
<h2>조회·신청 방법</h2>
<ol>
<li>The건강보험 앱 또는 nhis.or.kr 로그인</li>
<li>환급금·본인부담상한액 관련 메뉴 조회</li>
<li>환급 대상이면 본인 명의 계좌 등록 후 신청</li>
</ol>
<h2>보험료 환급과 구분</h2>
<table>
<tr><th>구분</th><th>내용</th></tr>
<tr><td>보험료 환급</td><td>과오납·자격변동 등으로 낸 보험료를 돌려줌</td></tr>
<tr><td>상한제 환급</td><td>의료비 본인부담 초과분을 돌려줌</td></tr>
</table>
<h2>주의할 점</h2>
<ul>
<li>“상한제 환급 클릭” 문자는 사칭일 수 있음 → 앱으로 직접 조회</li>
<li>실손보험과 중복 정산 여부를 각자 약관·보험사에 확인</li>
<li>비급여는 상한제 대상이 아닌 경우가 많음</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>소득분위는 어디서 보나요?</h3>
<p>공단이 보험료 수준 등으로 구간을 적용합니다. 앱·고객센터에서 본인 상한액을 확인할 수 있습니다.</p>
<h3>자동으로 들어오나요?</h3>
<p>사전급여는 병원 단계에서 처리되고, 사후정산은 계좌 등록·신청이 필요한 경우가 있습니다.</p>
""",
},
{
"file": "unemployment-leaving-code.html",
"title": "실업급여 이직확인서 이직사유 코드 보는 법",
"desc": "실업급여 심사에 중요한 이직확인서 이직사유, 회사 기재와 다를 때 대처, 자진퇴사·권고사직 구분 요령을 정리했습니다.",
"related": [
("실업급여 신청조건과 신청방법", "/unemployment-benefit.html"),
("자발적 퇴사 시 실업급여 가능 여부", "/unemployment-voluntary.html"),
("고용보험 가입이력 조회", "/employment-insurance.html"),
("근로장려금 신청방법", "/earned-income-credit.html"),
],
"official": [
("고용24", "https://www.work24.go.kr"),
],
"intro": """<h1>실업급여 이직확인서 이직사유 코드 보는 법</h1>
<p>실업급여 심사의 핵심 서류가 <strong>이직확인서</strong>입니다. 회사가 적은 이직사유가 “개인 사정 퇴직”이면 불리하고, 권고사직·계약만료·사업장 사정 등이면 유리한 경우가 많습니다. 퇴사 후 반드시 사유를 확인하세요.</p>
""",
"rest": """<h2>이직확인서란?</h2>
<p>사업주가 고용센터(고용보험)에 제출하는 퇴직 관련 공식 기록입니다. 피보험자격 상실일, 근무기간, <strong>이직사유</strong> 등이 담깁니다. 근로자는 고용24 등에서 내 이직 정보를 확인할 수 있습니다.</p>
<h2>왜 코드·사유가 중요한가</h2>
<ul>
<li>수급자격 “비자발적 이직” 판단의 1차 근거</li>
<li>자진퇴사로 기재되면 정당한 사유 증빙이 더 필요</li>
<li>회사 기재가 사실과 다르면 이의·정정 요청 가능</li>
</ul>
<h2>확인 순서</h2>
<ol>
<li>고용24 로그인 → 고용보험·이직확인 관련 메뉴</li>
<li>상실일·이직사유 문구/코드 확인</li>
<li>사실과 다르면 회사 담당자·고용센터에 정정 요청</li>
<li>체불·괴롭힘 등 사유면 별도 증빙 제출</li>
</ol>
<h2>자주 나오는 상황</h2>
<table>
<tr><th>상황</th><th>확인할 점</th></tr>
<tr><td>권고사직</td><td>면담기록, 사직서 문구, 회사 통보</td></tr>
<tr><td>계약만료</td><td>근로계약서 종료일</td></tr>
<tr><td>자진퇴사</td><td>정당한 이직사유 해당 여부·증빙</td></tr>
<tr><td>폐업·감원</td><td>사업장 사정 이직으로 기재됐는지</td></tr>
</table>
<h2>회사가 안 해주면</h2>
<p>사업주가 이직확인서 제출을 지연하면 고용센터에 신고·독촉할 수 있습니다. 수급 신청은 지연되더라도, 자격·기한은 상담으로 확인하세요.</p>
<h2>자주 묻는 질문</h2>
<h3>사직서에 “일신상 사유”만 썼어요</h3>
<p>이직확인서도 비슷하게 나가면 불리합니다. 실제 사유 증빙을 보강하고 센터 상담을 받으세요.</p>
<h3>코드 번호를 외워야 하나요?</h3>
<p>번호보다 <strong>기재된 사유 내용이 사실과 일치하는지</strong>가 중요합니다.</p>
""",
},
{
"file": "energy-vs-electricity.html",
"title": "에너지바우처 vs 전기요금 할인 차이",
"desc": "에너지바우처와 한국전력 전기요금 할인의 대상·신청처·중복 가능 여부·사용 방식을 비교해 정리했습니다.",
"related": [
("에너지바우처 신청방법", "/energy-voucher.html"),
("전기요금 할인 신청방법", "/electricity-discount.html"),
("기초생활수급자 혜택", "/basic-livelihood.html"),
("통신비 감면 신청방법", "/telecom-discount.html"),
],
"official": [
("에너지바우처", "https://www.energyvoucher.or.kr"),
("한국전력", "https://www.kepco.co.kr"),
("복지로", "https://www.bokjiro.go.kr"),
],
"intro": """<h1>에너지바우처 vs 전기요금 할인 차이</h1>
<p>둘 다 “전기·난방비를 줄여준다”는 점은 비슷하지만, <strong>주관 기관·신청 방법·지원 방식</strong>이 다릅니다. 수급자·차상위라면 둘 다 해당되는지 각각 확인하는 것이 좋습니다.</p>
""",
"rest": """<h2>한눈에 비교</h2>
<table>
<tr><th>구분</th><th>에너지바우처</th><th>전기요금 할인</th></tr>
<tr><td>주관</td><td>복지·에너지 바우처 사업</td><td>한국전력 요금 감면</td></tr>
<tr><td>지원</td><td>연간 한도(요금차감·카드)</td><td>매월 요금 할인율·할인한도</td></tr>
<tr><td>신청</td><td>행정복지센터·복지로 등</td><td>한전 고객센터·사이버지점</td></tr>
<tr><td>대상</td><td>기초수급 취약가구 중심</td><td>수급·차상위·장애인·다자녀 등</td></tr>
</table>
<h2>에너지바우처의 특징</h2>
<ul>
<li>전기뿐 아니라 가스·등유·LPG 등에도 사용 가능(방식에 따라)</li>
<li>신청·사용 <strong>기간</strong>이 정해진 경우가 많음</li>
<li>요금차감형 / 국민행복카드형으로 나뉨</li>
</ul>
<h2>전기요금 할인의 특징</h2>
<ul>
<li>한전 고객번호(계약) 단위로 적용</li>
<li>이사하면 재신청이 필요한 경우가 많음</li>
<li>복지 증명서류로 통신사·가스와 별개로 신청</li>
</ul>
<h2>중복이 되나?</h2>
<p>제도가 다르므로 <strong>요건만 맞으면 동시 적용 가능한 경우가 많습니다.</strong> 다만 바우처 차감과 요금 할인이 고지서에 어떻게 표시되는지는 한전·바우처 안내를 함께 보세요.</p>
<h2>무엇을 먼저?</h2>
<ol>
<li>기초수급·차상위 자격이 있으면 전기요금 할인부터 한전에 신청</li>
<li>하절기·동절기 바우처 모집 기간에 주민센터·복지로 신청</li>
<li>등유·LPG를 쓰면 바우처 카드형을 꼭 확인</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>바우처만 받으면 전기 할인은 안 되나요?</h3>
<p>아닙니다. 별도 제도이므로 한전 할인 요건이면 함께 신청하세요.</p>
<h3>통신비 감면도 비슷한가요?</h3>
<p>신청처가 통신사라는 점만 다르고, 복지 자격 연동은 비슷합니다.</p>
""",
},
{
"file": "year-end-refund-tips.html",
"title": "연말정산 환급 늘리는 공제 체크리스트",
"desc": "연말정산 환급을 놓치지 않기 위한 인적공제·카드·의료비·연금저축·월세 등 체크리스트를 정리했습니다.",
"related": [
("연말정산 환급금 조회", "/year-end-tax-refund.html"),
("근로장려금 신청방법", "/earned-income-credit.html"),
("자녀장려금 신청자격", "/child-tax-credit.html"),
("건강보험 환급금 조회", "/health-insurance-refund.html"),
],
"official": [
("국세청 홈택스", "https://www.hometax.go.kr"),
("연말정산 간소화", "https://www.hometax.go.kr"),
],
"intro": """<h1>연말정산 환급 늘리는 공제 체크리스트</h1>
<p>환급액이 적으면 “원래 그런가” 하고 넘기기 쉽습니다. 실제로는 <strong>간소화에 안 뜬 공제</strong>나 부양가족·월세·기부금을 빠뜨린 경우가 많습니다. 제출 전에 아래 목록으로 한 번 더 확인하세요.</p>
""",
"rest": """<h2>기본 체크</h2>
<ul>
<li>본인·배우자·부양가족 <strong>인적공제</strong> (나이·소득 요건)</li>
<li>장애인·경로우대 등 추가 공제 해당 여부</li>
<li>회사 연말정산 일정·마감일</li>
</ul>
<h2>자주 누락되는 항목</h2>
<ol>
<li><strong>월세액 공제</strong> — 무주택 근로자, 계약서·송금 증빙</li>
<li><strong>의료비</strong> — 난임·장애인 의료비, 간소화 누락분 영수증</li>
<li><strong>교육비</strong> — 학원비는 제한, 교복·체험학습 등 요건 확인</li>
<li><strong>기부금</strong> — 종교단체·지정기부금 영수증</li>
<li><strong>연금저축·IRP</strong> — 납입액 공제 한도</li>
<li><strong>보험료</strong> — 보장성 보험, 장애인전용</li>
</ol>
<h2>카드·현금영수증</h2>
<p>신용카드·체크카드·현금영수증은 사용액 구간에 따라 공제율이 다릅니다. 전통시장·대중교통 사용분이 반영됐는지 간소화에서 확인하세요.</p>
<h2>환급이 안 늘어나는 이유</h2>
<ul>
<li>이미 매월 원천징수가 적어 추가 환급 여지가 없음</li>
<li>소득·공제 변동으로 환급이 아니라 추가 납부</li>
<li>간소화만 믿고 누락 영수증을 안 넣음</li>
</ul>
<h2>실무 순서</h2>
<ol>
<li>1월 간소화 PDF·파일 내려받기</li>
<li>누락 항목 영수증 수집</li>
<li>홈택스 공제 신고서 미리 작성(가능 시)</li>
<li>회사에 제출 후 3~4월 환급 반영 확인</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>프리랜서도 연말정산하나요?</h3>
<p>근로소득만 연말정산 대상인 경우가 많고, 사업소득은 종합소득세 신고로 정산합니다.</p>
<h3>작년 놓친 공제는?</h3>
<p>경정청구 등으로 돌려받을 수 있는 경우가 있습니다. 홈택스·세무사 상담을 검토하세요.</p>
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

    patch_related("basic-pension.html", [
        ("기초연금 소득인정액 계산 쉽게 보기", "/basic-pension-income.html"),
    ])
    patch_related("basic-pension-rejection.html", [
        ("기초연금 소득인정액 계산 쉽게 보기", "/basic-pension-income.html"),
    ])
    patch_related("earned-income-credit.html", [
        ("단독·홑벌이·맞벌이 소득 기준", "/earned-income-household.html"),
    ])
    patch_related("earned-income-2026.html", [
        ("단독·홑벌이·맞벌이 소득 기준", "/earned-income-household.html"),
    ])
    patch_related("health-insurance-refund.html", [
        ("본인부담상한제 환급 시기", "/health-copay-cap.html"),
    ])
    patch_related("health-refund-scam.html", [
        ("본인부담상한제 환급 시기", "/health-copay-cap.html"),
    ])
    patch_related("unemployment-benefit.html", [
        ("이직확인서 이직사유 코드 보는 법", "/unemployment-leaving-code.html"),
    ])
    patch_related("unemployment-voluntary.html", [
        ("이직확인서 이직사유 코드 보는 법", "/unemployment-leaving-code.html"),
    ])
    patch_related("energy-voucher.html", [
        ("에너지바우처 vs 전기요금 할인", "/energy-vs-electricity.html"),
    ])
    patch_related("electricity-discount.html", [
        ("에너지바우처 vs 전기요금 할인", "/energy-vs-electricity.html"),
    ])
    patch_related("year-end-tax-refund.html", [
        ("연말정산 환급 늘리는 체크리스트", "/year-end-refund-tips.html"),
    ])


if __name__ == "__main__":
    main()
