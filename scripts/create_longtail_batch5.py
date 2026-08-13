#!/usr/bin/env python3
"""Batch 5: five readable long-tail articles focused on dwell time."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.juho15.com"
UPDATE = "2026년 8월 13일"
UPDATE_ISO = "2026-08-13"
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
"file": "basic-pension-spouse-death.html",
"title": "배우자 사망 후 기초연금·유족연금 확인 순서",
"desc": "배우자 사후 기초연금 자격 변동, 국민연금 유족연금, 서류·신청 순서를 상황별로 쉽게 정리했습니다.",
"related": [
("부부 기초연금 신청 시 확인", "/basic-pension-couple.html"),
("기초연금 재신청 시기", "/basic-pension-reapply-timing.html"),
("기초연금 소득인정액 계산", "/basic-pension-income.html"),
("국민연금 예상수령액 조회", "/national-pension.html"),
],
"official": [
("복지로", "https://www.bokjiro.go.kr"),
("보건복지부 기초연금", "https://basicpension.mohw.go.kr"),
("국민연금공단", "https://www.nps.or.kr"),
],
"intro": """<h1>배우자 사망 후 기초연금·유족연금 확인 순서</h1>
<p>배우자를 여의면 장례·상속 일로도 바쁘지만, <strong>기초연금·국민연금</strong>은 가구 구성이 바뀌는 순간 자격이 달라질 수 있습니다. “무엇을 먼저 해야 하지?”가 가장 흔한 질문입니다. 이 글은 복잡한 법령 대신, <strong>확인 순서</strong>만 차분히 따라가도록 썼습니다.</p>
<p>한 번에 다 신청하려 하지 마세요. 아래 순서로 보면 놓치는 항목이 줄어듭니다.</p>
""",
"rest": """<h2>이런 분은 여기부터</h2>
<ul>
<li>부부 중 한 분만 기초연금을 받고 있었는데 배우자가 사망한 경우</li>
<li>둘 다 기초연금을 받다가 가구원이 줄었 경우</li>
<li>국민연금 가입·수급 이력이 있어 유족연금 여부를 모르는 경우</li>
</ul>

<h2>한눈에 보는 확인 순서</h2>
<ol>
<li><strong>국민연금</strong> — 유족연금·사망일시금 해당 여부부터 조회</li>
<li><strong>기초연금</strong> — 행정복지센터·복지로에서 가구 변동 신고·재심사</li>
<li><strong>소득·재산</strong> — 상속·예금 명의 변경이 소득인정액에 영향을 주는지 점검</li>
<li><strong>연계 혜택</strong> — 통신·전기 할인, 노인일자리 등 가구 기준 혜택 재확인</li>
</ol>
<p>기초연금만 급하게 재신청하고 유족연금을 놓치는 경우가 있습니다. <a href="/national-pension.html">국민연금 조회</a>를 먼저 해 두면 이후 상담이 훨씬 수월합니다.</p>

<h2>기초연금에서 달라지는 점</h2>
<p>부부가구 기준과 단독가구 기준은 소득·재산 한도가 다릅니다. 배우자가 돌아가시면 가구 유형이 바뀌어 <strong>새로 받을 수 있게 되거나</strong>, 반대로 감액·중단 심사가 다시 열릴 수 있습니다.</p>
<ul>
<li>기존에 부부 감액을 받고 있었다면 단독 기준으로 재산정</li>
<li>배우자가 받던 금액이 끊기므로, 본인 수급액·자격만 따로 확인</li>
<li>상속 재산·보험금이 생기면 <a href="/basic-pension-income.html">소득인정액</a>이 올라갈 수 있음</li>
</ul>
<p>자세한 부부 기준은 <a href="/basic-pension-couple.html">부부 기초연금 가이드</a>를, 탈락 후 다시 넣는 타이밍은 <a href="/basic-pension-reapply-timing.html">재신청 시기</a>를 참고하세요.</p>

<h2>국민연금 유족연금은 별개</h2>
<p>기초연금과 국민연금 유족연금은 <strong>다른 제도</strong>입니다. 배우자가 국민연금 가입·수급 요건을 충족했다면 유족에게 연금이 지급될 수 있습니다. 요건·금액은 가입 기간·연령에 따라 달라지므로 공단 상담이 필요합니다.</p>
<table>
<tr><th>구분</th><th>기초연금</th><th>국민연금 유족연금</th></tr>
<tr><td>담당</td><td>복지부·지자체</td><td>국민연금공단</td></tr>
<tr><td>핵심</td><td>고령·소득인정액</td><td>가입·수급 이력·유족 요건</td></tr>
<tr><td>신청</td><td>행정복지센터·복지로</td><td>공단·내연금</td></tr>
</table>

<h2>자주 하는 실수</h2>
<ul>
<li>사망신고만 하고 복지·연금 쪽은 “자동으로 될 것”이라고 기다리는 경우</li>
<li>유족연금과 기초연금을 같은 창구로 착각하는 경우</li>
<li>상속 재산이 반영되기 전에 신청해 나중에 감액·환수되는 경우</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>장례가 끝나기 전에 신청해도 되나요?</h3>
<p>상담·서류 준비는 가능합니다. 다만 사망 사실이 행정에 반영된 뒤 심사가 진행되는 경우가 많으니, 센터·공단에 “지금 접수 가능한지”를 먼저 물어보세요.</p>
<h3>기초연금과 유족연금을 같이 받을 수 있나요?</h3>
<p>제도가 다르므로 각각 요건을 충족하면 병행될 수 있습니다. 다만 소득·수급 구조에 따라 실수령액이 달라질 수 있어 공식 상담이 안전합니다.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li>국민연금공단에서 유족연금 해당 여부 조회</li>
<li>복지로·행정복지센터에서 기초연금 가구 변동 상담</li>
<li>사이트 내 <a href="/basic-pension.html">기초연금 총정리</a>로 서류 목록 재확인</li>
</ol>
""",
},
{
"file": "earned-income-delay.html",
"title": "근로장려금 지급이 늦을 때 확인하는 방법",
"desc": "근로장려금 입금이 안 될 때 심사·계좌·안내문 상태 확인 순서와 국세청 조회 방법을 읽기 쉽게 정리했습니다.",
"related": [
("근로장려금 2026 신청기간", "/earned-income-2026.html"),
("근로장려금 안내문 없이 신청", "/earned-income-no-letter.html"),
("근로장려금 환수 대처", "/earned-income-repayment.html"),
("근로장려금 단독·맞벌이 기준", "/earned-income-household.html"),
],
"official": [
("국세청 홈택스", "https://www.hometax.go.kr"),
("국세청 장려금", "https://www.nts.go.kr"),
],
"intro": """<h1>근로장려금 지급이 늦을 때 확인하는 방법</h1>
<p>“신청은 했는데 통장에 안 들어온다.” 이때 대부분은 <strong>심사 중·계좌 오류·추가 자료 요청</strong> 중 하나입니다. 불안해서 여러 번 전화하기 전에, 홈택스에서 상태를 읽는 법부터 알아두면 시간을 아낄 수 있습니다.</p>
<p>이 글은 지급 일정을 약속하지 않습니다. 대신 <strong>어디서 무엇을 보면 되는지</strong>를 순서대로 안내합니다.</p>
""",
"rest": """<h2>먼저 마음 정리</h2>
<p>정기·반기 장려금은 신청 마감 후 <strong>일괄 심사</strong>를 거칩니다. 이웃은 받았는데 나만 늦는 경우도 흔합니다. “탈락”과 “아직 심사 중”은 홈택스 문구가 다릅니다.</p>

<h2>5분 체크리스트</h2>
<ol>
<li>홈택스 → 장려금·연말정산·전자기부금 → <strong>근로·자녀장려금</strong> 진행상태</li>
<li>신청한 회차(정기/반기)와 귀속연도가 맞는지</li>
<li>입금 계좌 예금주·계좌번호 오류·해지 여부</li>
<li>문자·우편으로 <strong>보완 요청</strong>이 왔는지</li>
<li>국세 체납·압류로 충당(상계)됐는지</li>
</ol>
<p>안내문을 못 받아 신청했다면 <a href="/earned-income-no-letter.html">안내문 없이 신청 가이드</a>도 함께 보세요. 일정 자체는 <a href="/earned-income-2026.html">2026 신청기간</a> 글을 참고하면 됩니다.</p>

<h2>상태가 이렇게 보이면</h2>
<table>
<tr><th>보이는 느낌</th><th>의미(일반적)</th><th>할 일</th></tr>
<tr><td>접수·심사중</td><td>아직 결정 전</td><td>보완 요청만 주기적으로 확인</td></tr>
<tr><td>지급결정·지급대기</td><td>곧 입금 또는 이체 준비</td><td>계좌·문자 알림 확인</td></tr>
<tr><td>지급제외·불승인</td><td>요건 미충족 등</td><td>사유 확인 후 이의·다음 회차</td></tr>
<tr><td>계좌오류</td><td>입금 실패</td><td>계좌 수정 후 재이체 안내 따름</td></tr>
</table>
<p>정확한 메뉴명은 홈택스 UI가 바뀔 수 있으니, 검색창에 “장려금”을 넣어 해당 서비스를 찾는 편이 빠릅니다.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>배우자 명의 계좌·이미 해지한 계좌를 그대로 둔 경우</li>
<li>반기 신청과 정기 신청을 혼동해 다른 회차를 기다리는 경우</li>
<li>환수·추징 안내를 지급 지연으로 오해하는 경우 → <a href="/earned-income-repayment.html">환수 대처</a></li>
</ul>

<h2>전화하기 전에 적을 것</h2>
<ul>
<li>신청 접수번호(또는 신청일)</li>
<li>주민등록상 주소·연락처</li>
<li>입금 예정 계좌 은행·끝자리</li>
<li>홈택스에 뜬 상태 문구 그대로</li>
</ul>
<p>준비되면 국세청 상담(126) 또는 홈택스 상담 채널을 이용하세요.</p>

<h2>자주 묻는 질문</h2>
<h3>자녀장려금만 오고 근로장려금이 없어요</h3>
<p>가구·소득 요건이 달라 한쪽만 지급될 수 있습니다. 홈택스에서 각각 결정 내용을 확인하세요.</p>
<h3>얼마가 들어오는지 미리 알 수 있나요?</h3>
<p>산정액은 심사 결과에 따릅니다. 예상액 조회가 열려 있으면 참고만 하고, 최종은 결정 통지를 기준으로 하세요.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://www.hometax.go.kr" rel="noopener noreferrer" target="_blank">홈택스</a>에서 장려금 진행상태</li>
<li>사이트 내 <a href="/earned-income-credit.html">근로장려금 신청 총정리</a></li>
<li>가구 유형이 헷갈리면 <a href="/earned-income-household.html">단독·홑벌이·맞벌이 기준</a></li>
</ol>
""",
},
{
"file": "national-pension-defer.html",
"title": "국민연금 납부예외·납부유예와 추후 영향",
"desc": "실직·소득 감소 시 국민연금 납부예외·유예 차이, 가입기간·연금액에 미치는 영향, 추후납부 연결을 쉽게 설명합니다.",
"related": [
("국민연금 공백·추후납부", "/national-pension-gap.html"),
("국민연금 조기·연기수령", "/national-pension-early.html"),
("국민연금 반환일시금", "/national-pension-lump-sum.html"),
("국민연금 예상수령액 조회", "/national-pension.html"),
],
"official": [
("국민연금공단", "https://www.nps.or.kr"),
("내연금", "https://www.nps.or.kr/jsppage/app/etc/easy.jsp"),
],
"intro": """<h1>국민연금 납부예외·납부유예와 추후 영향</h1>
<p>실직했거나 수입이 끊기면 “보험료를 어떻게 하지?”가 바로 따라옵니다. 이때 쓸 수 있는 제도가 <strong>납부예외</strong>와 <strong>납부유예(분할납부 등)</strong>입니다. 이름만 비슷하고 결과는 다릅니다.</p>
<p>이 글은 용어를 외우게 하기보다, <strong>지금 당장 부담을 줄일지 / 나중에 연금을 채울지</strong>를 기준으로 읽히게 구성했습니다.</p>
""",
"rest": """<h2>한 줄로 차이</h2>
<table>
<tr><th>제도</th><th>보험료</th><th>가입기간</th><th>나중에</th></tr>
<tr><td>납부예외</td><td>해당 기간 안 냄</td><td>원칙적으로 안 쌓임</td><td>추후납부로 메울 수 있는 경우 있음</td></tr>
<tr><td>납부유예·분할</td><td>나중에 냄</td><td>납부하면 반영</td><td>체납·이자 등 조건 확인</td></tr>
</table>
<p>자세한 공백 메우기는 <a href="/national-pension-gap.html">공백·추후납부 가이드</a>와 함께 보시면 이해가 빨라집니다.</p>

<h2>이런 상황에서 주로 씁니다</h2>
<ul>
<li>실업·휴직으로 소득이 거의 없을 때</li>
<li>사업 중단·폐업으로 지역가입 보험료가 부담될 때</li>
<li>군 입대·학업 등 법령상 예외 사유에 해당할 때(해당 시)</li>
</ul>

<h2>납부예외를 쓰기 전에 생각할 것</h2>
<p>당장은 편하지만, 예외 기간은 보통 <strong>가입 기간에 안 들어갑니다.</strong> 나중에 수급 요건(예: 최소 가입기간)을 채우지 못하면 연금 대신 다른 선택(일시금 등)을 보게 될 수 있습니다.</p>
<ol>
<li>내연금에서 현재 가입기간·예상수령액 조회</li>
<li>예외 신청 가능 사유·기간을 공단에 확인</li>
<li>예외 후 언제 추후납부할지 대략 계획</li>
</ol>
<p>조기·연기 수령을 고민 중이면 <a href="/national-pension-early.html">조기·연기 비교</a>도 같이 보세요. 가입기간이 짧을수록 선택지가 달라집니다.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>예외 신청을 안 하고 그냥 안 내다가 체납으로 쌓는 경우</li>
<li>예외 기간을 “자동으로 채워 줄 것”으로 착각</li>
<li>반환일시금만 보고 추후납부 기회를 놓침 → <a href="/national-pension-lump-sum.html">반환일시금 가이드</a></li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>직장가입자인데도 예외가 되나요?</h3>
<p>휴직·자격 변동 등 상황에 따라 다릅니다. 사업장 담당·공단에 자격 상태를 먼저 확인하세요.</p>
<h3>예외 후 보험료를 한꺼번에 내야 하나요?</h3>
<p>추후납부는 일시·분할 등 공단 안내에 따릅니다. 여유 자금을 보고 시기를 정하는 것이 좋습니다.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://www.nps.or.kr" rel="noopener noreferrer" target="_blank">국민연금공단</a> 상담·납부예외 안내</li>
<li>사이트 내 <a href="/national-pension.html">예상수령액 조회</a></li>
<li>공백을 메울 계획이 있으면 <a href="/national-pension-gap.html">추후납부</a></li>
</ol>
""",
},
{
"file": "health-dependent-change.html",
"title": "건강보험 피부양자 자격 상실·변경 시 대처",
"desc": "피부양자에서 지역가입자로 바뀔 때 보험료·신고 시기, 직장 피부양자 요건, 경감 신청까지 상황별로 정리했습니다.",
"related": [
("건강보험료 계산방법", "/health-insurance-premium.html"),
("건보료 경감·분할납부", "/health-premium-reduction.html"),
("건강보험 환급금 조회", "/health-insurance-refund.html"),
("환급금 사칭 문자 구별", "/health-refund-scam.html"),
],
"official": [
("국민건강보험공단", "https://www.nhis.or.kr"),
("The건강보험", "https://www.nhis.or.kr"),
],
"intro": """<h1>건강보험 피부양자 자격 상실·변경 시 대처</h1>
<p>부모님·배우자를 직장가입자 피부양자로 올렸다가, 어느 날 <strong>“자격이 상실됐다”</strong>는 안내를 받는 경우가 많습니다. 소득·재산·사업자 등록 기준이 바뀌면 자동으로 지역가입자로 전환될 수 있습니다.</p>
<p>당황하지 말고, <strong>왜 상실됐는지 → 보험료는 언제부터 → 경감·분할은 가능한지</strong> 순서로 보시면 됩니다.</p>
""",
"rest": """<h2>피부양자에서 빠지는 대표 이유</h2>
<ul>
<li>사업소득·이자·배당 등 일정 소득 초과</li>
<li>재산 기준 초과(공단 고시·안내 기준)</li>
<li>사업자등록·직장 가입 등으로 별도 자격이 생긴 경우</li>
<li>혼인·이혼·사망 등 가구 관계 변동</li>
</ul>
<p>정확한 기준은 해마다 달라질 수 있으니, 안내문에 적힌 사유 코드를 들고 <a href="https://www.nhis.or.kr" rel="noopener noreferrer" target="_blank">건강보험공단</a>에 확인하는 것이 가장 빠릅니다.</p>

<h2>상실 통보를 받으면 할 일</h2>
<ol>
<li>안내문의 <strong>상실 사유·적용 시점</strong> 확인</li>
<li>The건강보험·공단에서 지역가입자 보험료 고지 예정액 조회</li>
<li>소득·재산이 잘못 반영됐다면 정정·이의 신청</li>
<li>부담이 크면 <a href="/health-premium-reduction.html">경감·분할납부</a> 상담</li>
</ol>
<p>보험료 산정 원리가 궁금하면 <a href="/health-insurance-premium.html">건강보험료 계산</a> 글을 먼저 훑어보세요.</p>

<h2>직장 피부양자로 다시 올리려면</h2>
<p>요건을 다시 충족하면 직장가입자(자녀·배우자 등) 사업으로 피부양자 신고가 가능할 수 있습니다. 사업은 보통 <strong>사업장(회사) 담당</strong>을 통해 진행합니다.</p>
<ul>
<li>소득·재산이 기준 아래로 내려간 뒤 신고</li>
<li>필요 서류(가족관계·소득 입증 등) 준비</li>
<li>공단 심사 후 자격 취득일 확인</li>
</ul>

<h2>자주 하는 실수</h2>
<ul>
<li>상실 문자를 스팸으로 무시하다 체납이 쌓이는 경우</li>
<li>환급금 사칭 문자에 개인정보를 넘기는 경우 → <a href="/health-refund-scam.html">사칭 구별</a></li>
<li>고지서를 안 보고 “피부양자라서 무료”라고 착각</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>상실 직후 병원비는?</h3>
<p>자격이 지역가입자로 바뀌어도 보험 급여는 이어지는 것이 일반적입니다. 다만 보험료 납부·자격 공백이 있으면 불이익이 있을 수 있으니 공단에 확인하세요.</p>
<h3>과납한 보험료는?</h3>
<p>자격·보험료 정정 후 환급되는 경우가 있습니다. <a href="/health-insurance-refund.html">환급금 조회</a>도 함께 확인하세요.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li>공단 안내문 사유 확인 + The건강보험 조회</li>
<li>부담 시 <a href="/health-premium-reduction.html">경감·분할납부</a></li>
<li>회사 피부양자 재신고가 가능하면 인사·총무에 문의</li>
</ol>
""",
},
{
"file": "unemployment-documents.html",
"title": "실업급여 신청 전 준비 서류 체크리스트",
"desc": "실업급여 신청 전 이직확인서·신분증·계좌·구직신청까지 준비물과 순서를 체크리스트로 정리했습니다.",
"related": [
("실업급여 신청방법", "/unemployment-benefit.html"),
("이직확인서 이직사유", "/unemployment-leaving-code.html"),
("자발적 퇴사 시 실업급여", "/unemployment-voluntary.html"),
("실업급여 재취업·조기취업수당", "/unemployment-early-reemploy.html"),
],
"official": [
("고용보험", "https://www.ei.go.kr"),
("워크넷", "https://www.work.go.kr"),
("고용24", "https://www.work24.go.kr"),
],
"intro": """<h1>실업급여 신청 전 준비 서류 체크리스트</h1>
<p>실업급여는 “퇴사 다음날 바로”보다, <strong>서류와 구직신청이 갖춰진 뒤</strong>가 훨씬 수월합니다. 창구에서 한 번 더 오라는 말을 들으면 기운이 빠지죠. 그래서 이 글은 설명보다 <strong>체크리스트</strong> 비중을 높였습니다.</p>
<p>인쇄하거나 메모장에 옮겨 두고, 하나씩 지워 가며 준비해 보세요.</p>
""",
"rest": """<h2>신청 전 필수에 가까운 목록</h2>
<ul>
<li>□ 신분증 (주민등록증·운전면허 등)</li>
<li>□ 본인 명의 통장 계좌번호 (급여 입금용)</li>
<li>□ 이직확인서 처리 여부 확인 (전 직장·고용센터)</li>
<li>□ 고용보험 피보험 자격·이직일 확인</li>
<li>□ 워크넷·고용24 등 <strong>구직신청(구직등록)</strong> 완료</li>
</ul>
<p>이직확인서의 이직사유 코드는 심사에 직접 영향을 줍니다. 꼭 <a href="/unemployment-leaving-code.html">이직사유 가이드</a>를 먼저 읽어 보세요.</p>

<h2>상황에 따라 추가로 챙길 것</h2>
<table>
<tr><th>상황</th><th>추가 확인</th></tr>
<tr><td>권고사직·계약만료</td><td>퇴직 증명, 계약서, 통보 문자·메일</td></tr>
<tr><td>자발적 퇴사</td><td>정당한 사유 입증 자료 → <a href="/unemployment-voluntary.html">자발적 퇴사 가이드</a></td></tr>
<tr><td>질병·부상</td><td>진단서·소견서 등 (해당 시)</td></tr>
<tr><td>출산·육아 등</td><td>관련 입증 서류 (해당 시)</td></tr>
</table>

<h2>추천 진행 순서 (읽으면서 따라가기)</h2>
<ol>
<li>전 직장에 이직확인서 신고 여부 확인</li>
<li><a href="https://www.ei.go.kr" rel="noopener noreferrer" target="_blank">고용보험</a>에서 피보험 내역·이직일 조회</li>
<li><a href="https://www.work.go.kr" rel="noopener noreferrer" target="_blank">워크넷</a> 또는 <a href="https://www.work24.go.kr" rel="noopener noreferrer" target="_blank">고용24</a>에서 구직신청</li>
<li>거주지 관할 고용센터 방문·온라인 수급 자격 신청</li>
<li>이후 실업인정 일정에 맞춰 구직활동 기록</li>
</ol>
<p>전체 흐름은 <a href="/unemployment-benefit.html">실업급여 신청 총정리</a>에 더 자세히 있습니다.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>구직신청 없이 센터만 방문하는 경우</li>
<li>이직사유가 ‘개인사정’으로만 되어 있는데 자료를 안 챙긴 경우</li>
<li>수급 중 알바를 하고도 신고하지 않는 경우 → <a href="/unemployment-early-reemploy.html">재취업·조기취업수당</a></li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>이직확인서가 아직 안 올라왔어요</h3>
<p>전 직장에 독촉하고, 고용센터에 “미신고 시 처리”를 문의하세요. 일정 지연 사유가 됩니다.</p>
<h3>온라인만으로 끝나나요?</h3>
<p>초기 신청·교육·실업인정 방식은 센터·개인 상황에 따라 다릅니다. 앱·홈페이지 안내를 따르되, 막히면 관할 센터에 전화로 동선을 확인하세요.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://www.ei.go.kr" rel="noopener noreferrer" target="_blank">고용보험</a> 피보험·이직 조회</li>
<li>구직신청 후 관할 고용센터</li>
<li>사이트 내 <a href="/unemployment-benefit.html">신청 총정리</a> · <a href="/unemployment-leaving-code.html">이직사유</a></li>
</ol>
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
<p class="site-logo"><a href="/">주호15 인포</a></p>
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
"basic-pension.html": [("배우자 사망 후 기초·유족연금", "/basic-pension-spouse-death.html")],
"basic-pension-couple.html": [("배우자 사망 후 기초·유족연금", "/basic-pension-spouse-death.html")],
"earned-income-credit.html": [("근로장려금 지급이 늦을 때", "/earned-income-delay.html")],
"earned-income-2026.html": [("근로장려금 지급이 늦을 때", "/earned-income-delay.html")],
"national-pension.html": [("국민연금 납부예외·유예", "/national-pension-defer.html")],
"national-pension-gap.html": [("국민연금 납부예외·유예", "/national-pension-defer.html")],
"health-insurance-premium.html": [("피부양자 자격 상실·변경", "/health-dependent-change.html")],
"health-premium-reduction.html": [("피부양자 자격 상실·변경", "/health-dependent-change.html")],
"unemployment-benefit.html": [("실업급여 신청 전 서류", "/unemployment-documents.html")],
"unemployment-early-reemploy.html": [("실업급여 신청 전 서류", "/unemployment-documents.html")],
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
