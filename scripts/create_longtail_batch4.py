#!/usr/bin/env python3
"""Batch 4: ten new long-tail articles for active site maintenance."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.juho15.com"
UPDATE = "2026년 7월 24일"
UPDATE_ISO = "2026-07-24"
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
"file": "basic-pension-reapply-timing.html",
"title": "기초연금 재신청 시기와 소득·재산 변동 후 대처",
"desc": "기초연금 탈락·중단 후 재신청 타이밍, 소득·재산 감소 시 확인 포인트, 연중 신청 가능 여부를 정리했습니다.",
"related": [
("기초연금 탈락 이유와 재신청", "/basic-pension-rejection.html"),
("기초연금 소득인정액 계산", "/basic-pension-income.html"),
("부부 기초연금", "/basic-pension-couple.html"),
("기초연금 수급자격", "/basic-pension.html"),
],
"official": [("복지로", "https://www.bokjiro.go.kr"), ("보건복지부 기초연금", "https://basicpension.mohw.go.kr")],
"intro": """<h1>기초연금 재신청 시기와 소득·재산 변동 후 대처</h1>
<p>기초연금은 <strong>연중 상시 신청</strong>이 가능합니다. 한 번 탈락했거나 수급이 중단됐더라도, 소득·재산이 줄었거나 가구 구성이 바뀌면 다시 신청할 수 있습니다. “언제 다시 내면 되는지”만 정리해 둡니다.</p>
""",
"rest": """<h2>재신청이 유리한 경우</h2>
<ul>
<li>근로소득·사업소득이 줄었을 때</li>
<li>예금·보험·부동산 등 재산 처분·감소 후</li>
<li>배우자·동거 가족 변동으로 가구 소득인정액이 낮아질 때</li>
<li>부채(전세보증금 반환 등) 반영이 필요한 때</li>
</ul>
<h2>신청 시기 팁</h2>
<ol>
<li>변동 직후보다는 <strong>관련 서류가 준비된 뒤</strong> 신청</li>
<li>소득 조사는 최근 자료를 기준으로 하므로, 감소가 통장·신고에 반영됐는지 확인</li>
<li>탈락 사유 통지문을 보관해 두면 상담·재신청 시 도움이 됨</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>탈락 후 몇 개월을 기다려야 하나요?</h3>
<p>법정 대기 기간은 없습니다. 요건을 충족하면 바로 재신청할 수 있습니다.</p>
<h3>수급 중 소득이 늘면?</h3>
<p>정기·수시 조사로 감액·중단될 수 있습니다. 다시 요건을 충족하면 재신청하면 됩니다.</p>
""",
},
{
"file": "national-pension-lump-sum.html",
"title": "국민연금 반환일시금·일시금 수령 조건",
"desc": "국민연금 반환일시금 청구 요건, 국외이주·사망·수급연령 미달, 추후납부와의 선택 포인트를 정리했습니다.",
"related": [
("국민연금 예상수령액 조회", "/national-pension.html"),
("국민연금 공백·추후납부", "/national-pension-gap.html"),
("국민연금 조기·연기수령", "/national-pension-early.html"),
("퇴직연금 중도인출", "/retirement-pension-withdrawal.html"),
],
"official": [("국민연금공단", "https://www.nps.or.kr")],
"intro": """<h1>국민연금 반환일시금·일시금 수령 조건</h1>
<p>가입 기간이 짧거나 국외이주·사망 등으로 <strong>연금 대신 일시금</strong>을 받는 경우가 있습니다. 반환일시금과 일반 노령연금은 선택이 다르니, 청구 전에 조건을 확인하세요.</p>
""",
"rest": """<h2>반환일시금이 나오는 대표 경우</h2>
<ul>
<li>가입기간이 짧아 노령연금 수급요건을 못 채운 경우(요건은 공단 기준)</li>
<li>국외이주·국적 상실 등 법령상 사유</li>
<li>사망 시 유족에게 지급되는 경우(유족연금과 선택)</li>
</ul>
<h2>일시금 vs 추후납부</h2>
<table>
<tr><th>선택</th><th>특징</th></tr>
<tr><td>반환일시금</td><td>당장 목돈, 이후 연금 수급권은 제한될 수 있음</td></tr>
<tr><td>추후납부·가입 연장</td><td>기간을 채워 월 연금으로 받는 선택</td></tr>
</table>
<h2>청구 전 체크</h2>
<ol>
<li>내연금·공단 상담으로 예상 일시금·연금액 비교</li>
<li>유족·배우자 관련 선택 여부 확인</li>
<li>세무·건강보험 연계 영향은 개인 상황에 따라 다름</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>일시금 받고 나중에 다시 가입하면?</h3>
<p>제도·시점에 따라 재가입·추후납부 가능 여부가 달라집니다. 공단에서 확인하세요.</p>
""",
},
{
"file": "health-premium-reduction.html",
"title": "건강보험료 경감·분할납부 신청 방법",
"desc": "건보료가 부담될 때 경감·분할납부·체납 대처, 직장·지역가입자별 확인 경로를 정리했습니다.",
"related": [
("건강보험료 계산방법", "/health-insurance-premium.html"),
("건강보험 환급금 조회", "/health-insurance-refund.html"),
("본인부담상한제 환급", "/health-copay-cap.html"),
("환급금 사칭 문자 구별", "/health-refund-scam.html"),
],
"official": [("국민건강보험공단", "https://www.nhis.or.kr")],
"intro": """<h1>건강보험료 경감·분할납부 신청 방법</h1>
<p>소득 감소·실직·장기 체납으로 보험료가 부담되면 <strong>경감·분할납부·납부유예</strong>를 먼저 확인하세요. 직장가입자와 지역가입자 절차가 다릅니다.</p>
""",
"rest": """<h2>먼저 확인할 제도</h2>
<ul>
<li><strong>보험료 경감</strong> — 소득·재산·가구 상황에 따른 감면</li>
<li><strong>분할납부</strong> — 체납·일시 부담을 나눠 납부</li>
<li><strong>임의계속가입</strong> — 퇴직 후 직장보험 유지(요건 충족 시)</li>
</ul>
<h2>신청 경로</h2>
<ol>
<li>건강보험공단 지사·고객센터(1577-1000)</li>
<li>The건강보험 앱·홈페이지 민원</li>
<li>직장가입자는 사업장 담당자와 함께 자격 변동도 점검</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>체납하면 병원 이용이 막히나요?</h3>
<p>장기 체납 시 급여 제한이 있을 수 있습니다. 분할납부·납부 계획부터 상담하세요.</p>
<h3>환급금과 경감은 다른가요?</h3>
<p>환급은 과오납·상한제 등이고, 경감은 앞으로 낼 보험료를 줄이는 제도입니다.</p>
""",
},
{
"file": "unemployment-early-reemploy.html",
"title": "실업급여 수급 중 재취업과 조기취업수당",
"desc": "실업급여 받는 중 취업·알바 신고, 조기취업수당 요건, 수급 종료 후 재신청 포인트를 정리했습니다.",
"related": [
("실업급여 신청방법", "/unemployment-benefit.html"),
("자발적 퇴사 시 실업급여", "/unemployment-voluntary.html"),
("이직확인서 이직사유", "/unemployment-leaving-code.html"),
("고용보험 가입이력 조회", "/employment-insurance.html"),
],
"official": [("고용보험", "https://www.ei.go.kr"), ("워크넷", "https://www.work.go.kr")],
"intro": """<h1>실업급여 수급 중 재취업과 조기취업수당</h1>
<p>실업급여를 받는 중에도 <strong>취업·아르바이트</strong>가 가능하지만, 신고를 빠뜨리면 부정수급이 될 수 있습니다. 조기에 취업하면 조기취업수당도 검토해 보세요.</p>
""",
"rest": """<h2>재취업 시 필수</h2>
<ol>
<li>취업·근로 개시 전후 <strong>고용센터에 신고</strong></li>
<li>실업인정일에 취업 사실·소득 정확히 기재</li>
<li>부정수급 시 반환·추가징수·수급제한 가능</li>
</ol>
<h2>조기취업수당이란?</h2>
<p>남은 수급일수가 일정 기준 이상일 때 재취업하면, 잔여분의 일부를 일시금으로 받는 제도입니다. 요건·지급률은 고용센터 안내를 따릅니다.</p>
<h2>자주 묻는 질문</h2>
<h3>단기 알바도 신고하나요?</h3>
<p>네. 일용·단기도 근로 사실이 있으면 신고·실업인정에 반영해야 합니다.</p>
<h3>수급 종료 후 다시 실업하면?</h3>
<p>피보험 단위기간·이직 사유 등 요건을 새로 충족해야 합니다.</p>
""",
},
{
"file": "housing-benefit-owner.html",
"title": "자가주택 주거급여(수선유지급여) 신청 가이드",
"desc": "임차가 아닌 자가 거주 시 주거급여 수선유지급여 대상, 주택 노후도 조사, 신청 절차를 정리했습니다.",
"related": [
("주거급여 신청방법", "/housing-benefit.html"),
("주거급여 탈락 이유", "/housing-benefit-rejection.html"),
("기초수급 vs 차상위", "/basic-livelihood-vs-near-poor.html"),
("차상위계층 신청 방법", "/near-poor-application.html"),
],
"official": [("복지로", "https://www.bokjiro.go.kr"), ("마이홈", "https://www.myhome.go.kr")],
"intro": """<h1>자가주택 주거급여(수선유지급여) 신청 가이드</h1>
<p>주거급여는 월세만 해당되는 것이 아닙니다. <strong>자가·기타 소유 주택</strong>에 사는 저소득 가구는 주택 수선비용을 지원하는 수선유지급여를 받을 수 있습니다.</p>
""",
"rest": """<h2>임차급여 vs 수선유지급여</h2>
<table>
<tr><th>구분</th><th>임차급여</th><th>수선유지급여</th></tr>
<tr><td>주거 형태</td><td>전·월세 등 임차</td><td>자가 등 소유·거주</td></tr>
<tr><td>지원 방식</td><td>월 현금(임차료)</td><td>주택 보수·수선</td></tr>
<tr><td>조사</td><td>임대차·소득</td><td>주택 노후도·소득</td></tr>
</table>
<h2>신청 흐름</h2>
<ol>
<li>행정복지센터·복지로에서 주거급여 신청</li>
<li>소득·재산 조사</li>
<li>주택 상태 조사 후 수선 범위·시기 결정</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>집 주인이 본인인데 월세도 받나요?</h3>
<p>자가는 통상 수선유지급여 대상입니다. 임차급여와는 다릅니다.</p>
<h3>탈락했다면?</h3>
<p>소득 초과·주택 상태·거주 요건을 확인한 뒤 <a href="/housing-benefit-rejection.html">재신청 가이드</a>를 참고하세요.</p>
""",
},
{
"file": "disability-pension-vs-allowance.html",
"title": "장애인연금 vs 장애수당 차이와 신청 순서",
"desc": "장애인연금과 장애수당의 대상·중증 기준·중복 여부, 기초수급·차상위와의 관계를 비교해 정리했습니다.",
"related": [
("장애인연금 신청방법", "/disability-pension.html"),
("장애수당 지원대상", "/disability-allowance.html"),
("기초생활수급자 혜택", "/basic-livelihood.html"),
("차상위계층 혜택", "/near-poor-benefits.html"),
],
"official": [("복지로", "https://www.bokjiro.go.kr"), ("보건복지부", "https://www.mohw.go.kr")],
"intro": """<h1>장애인연금 vs 장애수당 차이와 신청 순서</h1>
<p>둘 다 장애 관련 현금 지원이지만 <strong>중증 여부·연령·소득</strong> 기준이 다릅니다. 어떤 제도부터 볼지 헷갈릴 때 비교표로 정리합니다.</p>
""",
"rest": """<h2>한눈에 비교</h2>
<table>
<tr><th>구분</th><th>장애인연금</th><th>장애수당</th></tr>
<tr><td>주 대상</td><td>중증장애·연령 요건</td><td>경증 등 장애수당 대상</td></tr>
<tr><td>소득</td><td>소득·재산 기준</td><td>기초·차상위 등과 연계</td></tr>
<tr><td>성격</td><td>연금형 지원</td><td>수당형 지원</td></tr>
</table>
<h2>신청 순서 추천</h2>
<ol>
<li>장애인등록·등급(정도) 확인</li>
<li>중증·연령에 해당하면 장애인연금 상담</li>
<li>해당 없으면 장애수당·기초·차상위 연계 확인</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>둘 다 동시에 받나요?</h3>
<p>일반적으로 제도 목적·대상이 달라 중복 수급은 제한됩니다. 관할 센터에서 확인하세요.</p>
""",
},
{
"file": "youth-savings-eligibility.html",
"title": "청년내일저축계좌 소득·연령 자격 확인",
"desc": "청년내일저축계좌 연령·소득·근로 요건, 중도해지·유지 조건, 신청 전 체크리스트를 정리했습니다.",
"related": [
("청년내일저축계좌", "/youth-savings-account.html"),
("근로장려금 신청방법", "/earned-income-credit.html"),
("국가장학금 신청방법", "/national-scholarship.html"),
("소상공인 지원금", "/small-business-support.html"),
],
"official": [("복지로", "https://www.bokjiro.go.kr"), ("자산형성지원", "https://www.hope4u.go.kr")],
"intro": """<h1>청년내일저축계좌 소득·연령 자격 확인</h1>
<p>청년내일저축계좌는 “청년이면 누구나”가 아닙니다. <strong>나이·소득·근로(사업)</strong> 요건을 동시에 충족해야 합니다. 신청 전 자격만 빠르게 점검하세요.</p>
""",
"rest": """<h2>신청 전 체크리스트</h2>
<ul>
<li>연령: 공고 기준 청년 연령대에 해당하는지</li>
<li>소득: 가구·본인 소득 상한(중위소득 등) 충족</li>
<li>근로·사업: 가입 기간 중 근로·사업 유지 요건</li>
<li>타 자산형성 중복 가입 여부</li>
</ul>
<h2>유지·해지 시 주의</h2>
<ol>
<li>매월 저축·근로 증빙을 빠뜨리면 적립·매칭에 영향</li>
<li>중도해지 시 정부지원금 환수 조건 확인</li>
<li>소득 변동으로 자격 유지가 어려워지면 센터 상담</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>알바만 해도 되나요?</h3>
<p>근로 인정 범위는 공고·지침에 따릅니다. 단시간·일용도 인정되는지 확인하세요.</p>
""",
},
{
"file": "national-scholarship-cut.html",
"title": "국가장학금 감액·탈락 시 확인사항",
"desc": "국가장학금 소득구간 변경, 성적·이수학점 미달, 이중지원 제한, 재신청·구제 절차를 정리했습니다.",
"related": [
("국가장학금 신청방법", "/national-scholarship.html"),
("교육급여 신청대상", "/education-benefit.html"),
("청년내일저축계좌 자격", "/youth-savings-eligibility.html"),
("근로장려금 신청방법", "/earned-income-credit.html"),
],
"official": [("한국장학재단", "https://www.kosaf.go.kr")],
"intro": """<h1>국가장학금 감액·탈락 시 확인사항</h1>
<p>국가장학금이 줄거나 탈락하면 대개 <strong>소득구간·성적·이수학점·이중지원</strong> 중 하나입니다. 사유를 확인한 뒤 다음 차수·학기에 대비하세요.</p>
""",
"rest": """<h2>감액·탈락 흔한 사유</h2>
<ul>
<li>가구 소득구간이 상향해 지원 구간이 바뀐 경우</li>
<li>직전 학기 성적·이수학점 미달</li>
<li>타 장학금과 이중지원 한도 초과</li>
<li>신청 기간·서류 미비</li>
</ul>
<h2>바로 할 일</h2>
<ol>
<li>장학재단 마이페이지에서 심사 결과·사유 확인</li>
<li>소득·가구원 정보 오류면 정정·재심사 요청</li>
<li>성적 미달이면 다음 학기 기준·구제 여부 확인</li>
</ol>
<h2>자주 묻는 질문</h2>
<h3>1차 탈락하면 2차는?</h3>
<p>차수별 일정에 따라 재신청·추가 선발이 가능합니다. 공고를 확인하세요.</p>
""",
},
{
"file": "cancer-screening-missed.html",
"title": "국가암검진 기간 놓쳤을 때 대처법",
"desc": "국가암검진 대상 연도에 못 받았을 때 연장·내년 대상, 본인부담, 일반건강검진과의 관계를 정리했습니다.",
"related": [
("국가암검진 대상자", "/cancer-screening.html"),
("국가건강검진 대상자", "/medical-checkup.html"),
("건강검진 놓쳤을 때", "/medical-checkup-missed.html"),
("본인부담상한제 환급", "/health-copay-cap.html"),
],
"official": [("국민건강보험공단", "https://www.nhis.or.kr"), ("국가암정보센터", "https://www.cancer.go.kr")],
"intro": """<h1>국가암검진 기간 놓쳤을 때 대처법</h1>
<p>암검진은 종류·출생연도에 따라 <strong>해당 연도</strong>에만 안내되는 경우가 많습니다. 기간을 놓쳤다면 연장 가능 여부와 내년 대상을 바로 확인하세요.</p>
""",
"rest": """<h2>놓쳤을 때 확인 순서</h2>
<ol>
<li>건보공단·The건강보험에서 올해 암검진 대상·예약 가능 여부 조회</li>
<li>의료기관에 당해 연도 잔여 일정 문의</li>
<li>불가하면 다음 주기(홀·짝수 출생 등) 일정 메모</li>
</ol>
<h2>일반건강검진과 다른 점</h2>
<ul>
<li>암검진은 위·대장·유방·자궁경부·폐 등 항목별 주기</li>
<li>일반검진을 받아도 암검진은 별도 예약이 필요할 수 있음</li>
</ul>
<h2>자주 묻는 질문</h2>
<h3>해당 연도를 넘기면 무료가 안 되나요?</h3>
<p>원칙적으로 해당 연도 대상입니다. 예외·연장은 공단·지자체 안내에 따릅니다.</p>
""",
},
{
"file": "electricity-discount-documents.html",
"title": "전기요금 복지할인 필요 서류와 신청 방법",
"desc": "기초수급·차상위·장애인 등 전기요금 할인 신청처, 한전 서류, 에너지바우처와의 병행 여부를 정리했습니다.",
"related": [
("전기요금 할인", "/electricity-discount.html"),
("에너지바우처 vs 전기할인", "/energy-vs-electricity.html"),
("에너지바우처 신청방법", "/energy-voucher.html"),
("통신비 감면 서류", "/telecom-discount-documents.html"),
],
"official": [("한국전력", "https://online.kepco.co.kr"), ("복지로", "https://www.bokjiro.go.kr")],
"intro": """<h1>전기요금 복지할인 필요 서류와 신청 방법</h1>
<p>전기요금 할인은 자격만 있어도 <strong>자동 적용되지 않는 경우</strong>가 많습니다. 한전·지자체에 서류를 내고 고객번호에 할인을 연결해야 합니다.</p>
""",
"rest": """<h2>신청이 필요한 대표 대상</h2>
<ul>
<li>기초생활수급·차상위계층</li>
<li>장애인·국가유공자 등 복지할인 대상</li>
<li>대가족·다자녀·생명유지장치 등(해당 시)</li>
</ul>
<h2>준비 서류·신청처</h2>
<ol>
<li>신분증, 복지자격 증명(수급자증명서 등)</li>
<li>전기요금 청구서의 고객번호·주소</li>
<li>한전 온라인·고객센터 또는 행정복지센터 안내</li>
</ol>
<h2>에너지바우처와 함께?</h2>
<p>할인(요금 차감)과 바우처(난방·냉방 지원)는 성격이 다릅니다. 요건이 되면 <a href="/energy-vs-electricity.html">둘 다 검토</a>하세요.</p>
<h2>자주 묻는 질문</h2>
<h3>이사하면?</h3>
<p>새 주소·고객번호로 할인을 다시 연결해야 하는 경우가 많습니다.</p>
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
"basic-pension.html": [("기초연금 재신청 시기", "/basic-pension-reapply-timing.html")],
"basic-pension-rejection.html": [("기초연금 재신청 시기", "/basic-pension-reapply-timing.html")],
"national-pension.html": [("국민연금 반환일시금", "/national-pension-lump-sum.html")],
"national-pension-gap.html": [("국민연금 반환일시금", "/national-pension-lump-sum.html")],
"health-insurance-premium.html": [("건보료 경감·분할납부", "/health-premium-reduction.html")],
"unemployment-benefit.html": [("실업급여 재취업·조기취업수당", "/unemployment-early-reemploy.html")],
"housing-benefit.html": [("자가 주거급여(수선유지)", "/housing-benefit-owner.html")],
"disability-pension.html": [("장애인연금 vs 장애수당", "/disability-pension-vs-allowance.html")],
"disability-allowance.html": [("장애인연금 vs 장애수당", "/disability-pension-vs-allowance.html")],
"youth-savings-account.html": [("청년내일저축 자격 확인", "/youth-savings-eligibility.html")],
"national-scholarship.html": [("국가장학금 감액·탈락", "/national-scholarship-cut.html")],
"cancer-screening.html": [("암검진 놓쳤을 때", "/cancer-screening-missed.html")],
"electricity-discount.html": [("전기요금 할인 서류", "/electricity-discount-documents.html")],
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
