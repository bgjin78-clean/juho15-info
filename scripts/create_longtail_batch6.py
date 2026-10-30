#!/usr/bin/env python3
"""Batch 6: ten seasonal long-tail articles (autumn/winter search demand)."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import create_longtail_batch5 as base

base.UPDATE = "2026년 10월 30일"
base.UPDATE_ISO = "2026-10-30"
ROOT = base.ROOT
SITE = base.SITE
LASTMOD = base.UPDATE_ISO

ARTICLES = [
{
"file": "year-end-preview.html",
"title": "연말정산 미리보기로 11~12월에 환급 늘리는 법",
"desc": "홈택스 연말정산 미리보기로 예상 세액을 확인하고, 남은 두 달 동안 카드 사용·연금저축·기부금으로 환급을 늘리는 순서를 정리했습니다.",
"search": "연말정산 미리보기 11월 12월 환급 카드 연금저축 IRP",
"related": [
("연말정산 환급 늘리는 체크리스트", "/year-end-refund-tips.html"),
("연말정산 환급금 조회", "/year-end-tax-refund.html"),
("적금 이자 계산 방법", "/savings-interest.html"),
("퇴직연금 조회방법", "/retirement-pension.html"),
],
"official": [
("국세청 홈택스", "https://www.hometax.go.kr"),
("국세청", "https://www.nts.go.kr"),
],
"hubs": ["year-end-refund-tips.html", "year-end-tax-refund.html"],
"intro": """<h1>연말정산 미리보기로 11~12월에 환급 늘리는 법</h1>
<p>연말정산은 1월에 하는 일처럼 보이지만, 결과는 <strong>12월 31일까지 쓴 돈과 넣은 돈</strong>으로 이미 정해집니다. 1월에 서류를 아무리 잘 내도 지난해 사용 내역은 바꿀 수 없죠.</p>
<p>그래서 10~11월에 홈택스 <strong>연말정산 미리보기</strong>로 예상 세액을 한 번 보고, 남은 두 달을 어떻게 쓸지 정하는 것이 가장 효과적입니다. 이 글은 그 순서를 따라가도록 썼습니다.</p>
<div class="tool-box">
<p><strong>연말정산 예상 환급액 바로 계산</strong></p>
<p>총급여와 주요 공제 항목을 넣어 대략적인 결정세액을 확인해 보세요. 결과는 참고용입니다.</p>
<p><a href="https://calculator.juho15.com/year-end" rel="noopener noreferrer" target="_blank">금융계산기 — 연말정산 계산 열기</a></p>
</div>
""",
"rest": """<h2>이런 분은 여기부터</h2>
<ul>
<li>작년에 연말정산에서 세금을 토해 낸(추가 납부) 경험이 있는 분</li>
<li>올해 이직·연봉 변동이 있어 예상이 안 되는 분</li>
<li>연금저축·IRP를 넣을지 말지 고민 중인 분</li>
</ul>

<h2>미리보기에서 확인할 3가지</h2>
<ol>
<li><strong>1~9월 카드 사용액</strong> — 홈택스에 반영된 실제 사용액</li>
<li><strong>예상 결정세액</strong> — 올해 낼 세금 총액</li>
<li><strong>기납부세액과 차이</strong> — 매달 월급에서 떼인 세금과 비교해 환급/추가납부 판단</li>
</ol>
<p>메뉴 위치는 바뀔 수 있으니 홈택스 검색창에 “연말정산 미리보기”를 입력하는 편이 빠릅니다.</p>

<h2>남은 두 달, 무엇을 조정할까</h2>
<table>
<tr><th>항목</th><th>확인 포인트</th><th>조정 방법</th></tr>
<tr><td>신용카드 vs 체크카드</td><td>총급여의 25% 초과분부터 공제</td><td>25%를 넘었다면 공제율 높은 체크카드·현금영수증 위주로</td></tr>
<tr><td>전통시장·대중교통</td><td>별도 공제율·한도</td><td>교통비·장보기 결제 수단 점검</td></tr>
<tr><td>연금저축·IRP</td><td>세액공제 한도 내 납입</td><td>12월 말 전 납입분까지 반영</td></tr>
<tr><td>기부금</td><td>영수증 발급 기관인지</td><td>연말 기부 시 영수증 확인</td></tr>
</table>
<p>공제 항목 전체 목록은 <a href="/year-end-refund-tips.html">연말정산 환급 체크리스트</a>에 더 자세히 정리해 두었습니다.</p>

<h2>짧은 예시로 감 잡기</h2>
<p>총급여 4,000만 원인 직장인이라면 카드 사용액이 1,000만 원(25%)을 넘는 순간부터 공제가 시작됩니다. 9월까지 이미 1,100만 원을 썼다면, 남은 소비는 신용카드보다 공제율이 높은 체크카드로 돌리는 것이 유리할 수 있습니다. 반대로 아직 25%에 못 미쳤다면 결제 수단보다 “문턱 넘기”가 먼저입니다.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>1월에 가서야 미리보기를 확인해 조정할 시간이 없는 경우</li>
<li>연금저축을 12월 31일 이후에 넣어 올해 공제를 놓치는 경우</li>
<li>세액공제 한도를 넘게 넣고 “다 공제될 것”이라 생각하는 경우</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>미리보기 금액이 실제 결과와 같나요?</h3>
<p>아닙니다. 10~12월 사용액과 회사 제출 자료가 반영되지 않은 추정치입니다. 방향을 잡는 용도로 보세요.</p>
<h3>이직했으면 어떻게 하나요?</h3>
<p>전 직장 원천징수영수증을 현 직장에 제출해야 합산 정산이 됩니다. 미리보기에도 전 직장 소득이 빠져 있을 수 있습니다.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://www.hometax.go.kr" rel="noopener noreferrer" target="_blank">홈택스</a> 연말정산 미리보기</li>
<li><a href="https://calculator.juho15.com/year-end" rel="noopener noreferrer" target="_blank">연말정산 계산기</a>로 시나리오 비교</li>
<li>1월 이후에는 <a href="/year-end-tax-refund.html">환급금 조회</a></li>
</ol>
""",
},
{
"file": "parental-leave-benefit.html",
"title": "육아휴직급여 신청방법과 월 수령액 확인",
"desc": "육아휴직급여 신청 시기, 고용24 신청 순서, 기간별 지급액 구조와 부모 함께 육아휴직 시 확인할 점을 정리했습니다.",
"search": "육아휴직급여 육아휴직 신청 수령액 고용24 6+6",
"related": [
("부모급여·첫만남이용권 정리", "/parent-benefit.html"),
("고용보험 가입이력 조회", "/employment-insurance.html"),
("연말정산 미리보기", "/year-end-preview.html"),
("한부모가족 지원금", "/single-parent-support.html"),
],
"official": [
("고용24", "https://www.work24.go.kr"),
("고용보험", "https://www.ei.go.kr"),
("고용노동부", "https://www.moel.go.kr"),
],
"hubs": ["employment-insurance.html", "single-parent-support.html"],
"intro": """<h1>육아휴직급여 신청방법과 월 수령액 확인</h1>
<p>육아휴직을 결정하면 가장 먼저 드는 걱정은 “그동안 생활비는?”입니다. 육아휴직급여는 회사가 아니라 <strong>고용보험</strong>에서 나오고, <strong>직접 신청해야</strong> 받을 수 있습니다.</p>
<p>휴직 시작 전에 순서를 알아 두면, 첫 달 급여가 늦어지는 일을 줄일 수 있습니다.</p>
""",
"rest": """<h2>이런 분은 여기부터</h2>
<ul>
<li>육아휴직을 1~2개월 안에 시작할 예정인 분</li>
<li>배우자와 함께 또는 번갈아 휴직을 고민 중인 분</li>
<li>계약직·이직 이력이 있어 자격이 헷갈리는 분</li>
</ul>

<h2>기본 자격 체크</h2>
<ul>
<li>□ 고용보험 피보험 단위기간 합산 180일 이상</li>
<li>□ 만 8세 이하 또는 초등학교 2학년 이하 자녀 (기준은 공고 확인)</li>
<li>□ 회사에 육아휴직 신청 후 30일 이상 휴직</li>
</ul>
<p>가입 기간이 걱정되면 <a href="/employment-insurance.html">고용보험 가입이력 조회</a>로 먼저 확인하세요.</p>

<h2>신청 순서</h2>
<ol>
<li>회사에 육아휴직 신청 → 회사가 <strong>육아휴직 확인서</strong> 제출</li>
<li>휴직 시작 후 1개월 지나서 <a href="https://www.work24.go.kr" rel="noopener noreferrer" target="_blank">고용24</a>에서 급여 신청</li>
<li>매월(또는 몇 달치 모아서) 신청 — 휴직 종료 후 12개월 이내</li>
</ol>

<h2>월 지급액 구조 (최근 개편 기준)</h2>
<table>
<tr><th>기간</th><th>지급 구조(통상임금 대비)</th><th>비고</th></tr>
<tr><td>1~3개월</td><td>높은 비율·상한액</td><td>초기 소득 공백 완화</td></tr>
<tr><td>4~6개월</td><td>중간 비율·상한액</td><td>-</td></tr>
<tr><td>7개월 이후</td><td>낮은 비율·상한액</td><td>-</td></tr>
</table>
<p>2025년 개편 이후 상한액은 1~3개월 월 250만 원, 4~6개월 월 200만 원, 이후 월 160만 원 수준으로 안내되었습니다. 매년 바뀔 수 있으니 신청 전 <a href="https://www.moel.go.kr" rel="noopener noreferrer" target="_blank">고용노동부</a> 공지를 꼭 확인하세요.</p>

<h2>부모가 함께 휴직하면</h2>
<p>같은 자녀에 대해 부모가 모두 육아휴직을 쓰면 초기 몇 달간 상한액을 더 높여 주는 특례(이른바 6+6)가 운영됩니다. 시기를 맞추면 가계 부담이 크게 줄 수 있으니, 배우자 회사 일정까지 함께 계획해 보세요.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>회사가 확인서를 안 냈는데 본인만 신청해 처리 지연</li>
<li>휴직 중 다른 곳에서 소득이 생겼는데 신고하지 않음</li>
<li>휴직 종료 후 12개월이 지나 신청 기한을 놓침</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>사후지급금은 무엇인가요?</h3>
<p>급여 일부를 복직 후 일정 기간 근무하면 지급하던 방식입니다. 제도 개편 여부에 따라 달라지므로 신청 시점 안내를 확인하세요.</p>
<h3>부모급여와 같이 받을 수 있나요?</h3>
<p>제도가 다르므로 대상이면 함께 받을 수 있습니다. <a href="/parent-benefit.html">부모급여 정리</a>를 참고하세요.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li>회사 인사팀에 확인서 제출 일정 문의</li>
<li><a href="https://www.work24.go.kr" rel="noopener noreferrer" target="_blank">고용24</a> 육아휴직급여 신청</li>
<li>출산 직후라면 <a href="/parent-benefit.html">부모급여·첫만남이용권</a></li>
</ol>
""",
},
{
"file": "parent-benefit.html",
"title": "부모급여·첫만남이용권·아동수당 한 번에 정리",
"desc": "출산 후 받을 수 있는 부모급여, 첫만남이용권, 아동수당의 대상·금액·신청처를 비교표로 정리했습니다.",
"search": "부모급여 첫만남이용권 아동수당 출산 지원금 행복출산",
"related": [
("육아휴직급여 신청방법", "/parental-leave-benefit.html"),
("한부모가족 지원금", "/single-parent-support.html"),
("자녀장려금 신청자격", "/child-tax-credit.html"),
("청년도약계좌 정리", "/youth-leap-account.html"),
],
"official": [
("복지로", "https://www.bokjiro.go.kr"),
("정부24", "https://www.gov.kr"),
],
"hubs": ["single-parent-support.html", "child-tax-credit.html"],
"intro": """<h1>부모급여·첫만남이용권·아동수당 한 번에 정리</h1>
<p>아이가 태어나면 출생신고와 함께 <strong>여러 지원금</strong>을 신청할 수 있습니다. 이름이 비슷해서 “하나 신청하면 다 되는 줄” 알았다가 놓치는 경우가 많습니다.</p>
<p>이 글은 세 가지를 나란히 비교하고, 한 번에 신청하는 방법까지 안내합니다.</p>
""",
"rest": """<h2>한눈에 비교</h2>
<table>
<tr><th>제도</th><th>대상</th><th>지급 방식</th></tr>
<tr><td>첫만남이용권</td><td>출생아</td><td>바우처(첫째 200만 원, 둘째 이상 300만 원 수준)</td></tr>
<tr><td>부모급여</td><td>0~1세 아동</td><td>현금 월 지급(0세가 1세보다 많음)</td></tr>
<tr><td>아동수당</td><td>일정 연령 미만 아동</td><td>현금 월 10만 원 수준</td></tr>
</table>
<p>금액과 대상 연령은 정책 개편으로 바뀔 수 있습니다. 신청 직전 <a href="https://www.bokjiro.go.kr" rel="noopener noreferrer" target="_blank">복지로</a>에서 최신 기준을 확인하세요.</p>

<h2>가장 쉬운 신청법: 출생신고 때 한 번에</h2>
<p>주민센터에서 출생신고를 할 때 <strong>행복출산 원스톱 서비스</strong>를 요청하면 여러 지원을 한 번에 신청할 수 있습니다. 온라인은 정부24·복지로에서 가능합니다.</p>
<ol>
<li>출생신고 (주민센터 또는 온라인)</li>
<li>행복출산 원스톱으로 부모급여·아동수당·첫만남이용권 동시 신청</li>
<li>첫만남이용권은 국민행복카드로 지급되므로 카드 발급 확인</li>
</ol>

<h2>신청 시기가 중요한 이유</h2>
<p>부모급여·아동수당은 <strong>출생일 포함 60일 이내</strong>에 신청하면 출생월부터 소급 지급되는 것이 일반적입니다. 이 기간을 넘기면 신청한 달부터만 받을 수 있습니다.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>첫만남이용권 사용 기한을 넘겨 소멸</li>
<li>어린이집 이용 시 부모급여가 보육료로 전환되는 점을 모르는 경우</li>
<li>해외 체류 기간에 지급 정지되는 규정을 놓침</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>어린이집에 보내면 부모급여는?</h3>
<p>보육료 바우처로 일부 또는 전부가 전환되고, 차액이 있으면 현금으로 지급됩니다.</p>
<h3>육아휴직급여와 중복되나요?</h3>
<p>별개 제도라 함께 받을 수 있습니다. <a href="/parental-leave-benefit.html">육아휴직급여</a> 글을 참고하세요.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://www.gov.kr" rel="noopener noreferrer" target="_blank">정부24</a> 행복출산 원스톱</li>
<li><a href="https://www.bokjiro.go.kr" rel="noopener noreferrer" target="_blank">복지로</a> 지급 내역 조회</li>
<li>자녀가 크면 <a href="/child-tax-credit.html">자녀장려금</a>도 확인</li>
</ol>
""",
},
{
"file": "heating-cost-support.html",
"title": "겨울철 난방비 지원 총정리: 에너지바우처·등유·연탄",
"desc": "겨울 난방비 부담을 줄이는 에너지바우처, 등유바우처, 연탄쿠폰, 도시가스 요금 경감을 대상별로 비교했습니다.",
"search": "난방비 지원 등유바우처 연탄쿠폰 도시가스 감면 겨울",
"related": [
("에너지바우처 신청방법", "/energy-voucher.html"),
("에너지바우처 vs 전기요금 할인", "/energy-vs-electricity.html"),
("전기요금 할인 신청방법", "/electricity-discount.html"),
("긴급복지지원 신청", "/emergency-welfare.html"),
],
"official": [
("에너지바우처", "https://www.energyv.or.kr"),
("복지로", "https://www.bokjiro.go.kr"),
("한국에너지재단", "https://www.koref.or.kr"),
],
"hubs": ["energy-voucher.html", "energy-vs-electricity.html"],
"intro": """<h1>겨울철 난방비 지원 총정리: 에너지바우처·등유·연탄</h1>
<p>11월부터 고지서가 무거워집니다. 난방 방식이 집마다 달라서 <strong>받을 수 있는 지원도 다릅니다.</strong> 도시가스를 쓰는 집과 등유 보일러를 쓰는 집은 신청처부터 다르죠.</p>
<p>우리 집 난방 방식을 먼저 정하고, 아래 표에서 해당 줄만 따라가 보세요.</p>
""",
"rest": """<h2>난방 방식별 지원</h2>
<table>
<tr><th>난방 방식</th><th>주요 지원</th><th>신청처</th></tr>
<tr><td>도시가스</td><td>에너지바우처 차감, 도시가스 요금 경감</td><td>행정복지센터, 가스공급사</td></tr>
<tr><td>등유 보일러</td><td>등유바우처(국민행복카드)</td><td>행정복지센터</td></tr>
<tr><td>연탄</td><td>연탄쿠폰</td><td>행정복지센터</td></tr>
<tr><td>전기 난방</td><td>에너지바우처, 전기요금 복지할인</td><td>센터, 한전</td></tr>
</table>

<h2>에너지바우처가 기본</h2>
<p>생계·의료·주거·교육급여 수급 가구 중 노인, 장애인, 영유아, 임산부 등이 있는 가구가 주 대상입니다. 자세한 대상은 <a href="/energy-voucher.html">에너지바우처 가이드</a>에 정리했습니다. 전기요금 할인과 함께 받을 수 있는지 궁금하면 <a href="/energy-vs-electricity.html">비교 글</a>을 보세요.</p>

<h2>신청 전 체크리스트</h2>
<ul>
<li>□ 우리 집 난방 방식 (고지서·보일러 확인)</li>
<li>□ 수급자·차상위 여부</li>
<li>□ 가구원 중 65세 이상·장애인·영유아 여부</li>
<li>□ 신청 기간 (보통 연초~가을, 지자체 공고 확인)</li>
</ul>

<h2>수급자가 아니라면</h2>
<p>기준에 조금 못 미치더라도 갑작스러운 실직·질병으로 난방비가 어렵다면 <a href="/emergency-welfare.html">긴급복지지원</a>의 동절기 연료비 지원을 상담해 볼 수 있습니다. 지자체 자체 난방비 지원이 있는 경우도 많으니 주민센터에 꼭 문의하세요.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>에너지바우처를 신청만 하고 사용 기한 내에 쓰지 않음</li>
<li>이사 후 공급사가 바뀌었는데 변경 신청을 안 함</li>
<li>등유 사용 가구가 도시가스 경감만 알아보는 경우</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>바우처 잔액은 어떻게 확인하나요?</h3>
<p>에너지바우처 누리집이나 콜센터에서 조회할 수 있습니다.</p>
<h3>세입자도 받을 수 있나요?</h3>
<p>소유 여부가 아니라 가구 요건 기준입니다. 실거주하며 요금을 부담하면 대상이 될 수 있습니다.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://www.energyv.or.kr" rel="noopener noreferrer" target="_blank">에너지바우처</a> 대상·잔액 조회</li>
<li>사이트 내 <a href="/electricity-discount.html">전기요금 할인</a></li>
<li>갑자기 어려워졌다면 <a href="/emergency-welfare.html">긴급복지지원</a></li>
</ol>
""",
},
{
"file": "youth-rent-support.html",
"title": "청년 월세 지원 신청 자격과 준비 서류",
"desc": "청년 월세 특별지원의 나이·소득·재산 기준, 복지로 신청 순서, 거절되는 흔한 이유를 정리했습니다.",
"search": "청년 월세 지원 월세 특별지원 청년 주거 복지로 자격",
"related": [
("주거급여 신청방법", "/housing-benefit.html"),
("주거급여 탈락 이유", "/housing-benefit-rejection.html"),
("청년도약계좌 정리", "/youth-leap-account.html"),
("청년내일저축계좌", "/youth-savings-account.html"),
],
"official": [
("복지로", "https://www.bokjiro.go.kr"),
("마이홈포털", "https://www.myhome.go.kr"),
("국토교통부", "https://www.molit.go.kr"),
],
"hubs": ["housing-benefit.html", "youth-savings-account.html"],
"intro": """<h1>청년 월세 지원 신청 자격과 준비 서류</h1>
<p>월세가 월급의 상당 부분을 차지하는 청년이 많습니다. <strong>청년 월세 지원</strong>은 부모와 떨어져 사는 무주택 청년에게 월세 일부를 지원하는 제도입니다. 월 최대 20만 원 수준으로 운영되어 왔습니다.</p>
<p>문제는 <strong>소득 기준이 두 가지</strong>(청년 가구, 원가구)라 헷갈린다는 점입니다. 이 글은 자격을 단계별로 확인하게 구성했습니다.</p>
""",
"rest": """<h2>자격 3단계 확인</h2>
<ol>
<li><strong>나이·주거</strong> — 만 19~34세, 부모와 별도 거주, 무주택</li>
<li><strong>청년 가구 소득·재산</strong> — 중위소득 일정 비율 이하</li>
<li><strong>원가구(부모 포함) 소득·재산</strong> — 중위소득 일정 비율 이하</li>
</ol>
<p>임차보증금·월세 상한 조건도 있습니다. 해마다 공고 기준이 조금씩 바뀌므로 <a href="https://www.bokjiro.go.kr" rel="noopener noreferrer" target="_blank">복지로</a> 모의계산을 먼저 해 보세요.</p>

<h2>준비 서류</h2>
<ul>
<li>□ 임대차계약서 사본 (확정일자 권장)</li>
<li>□ 최근 월세 이체 내역</li>
<li>□ 신분증, 통장 사본</li>
<li>□ 소득 증빙 (필요 시)</li>
</ul>

<h2>주거급여와 무엇이 다를까</h2>
<table>
<tr><th>구분</th><th>청년 월세 지원</th><th>주거급여</th></tr>
<tr><td>대상</td><td>청년 독립 가구</td><td>소득 기준 충족 전 가구</td></tr>
<tr><td>기간</td><td>정해진 기간 한정</td><td>자격 유지 시 계속</td></tr>
<tr><td>중복</td><td colspan="2">주거급여 수급 시 중복 제한될 수 있음</td></tr>
</table>
<p>주거급여 대상인지도 함께 보려면 <a href="/housing-benefit.html">주거급여 가이드</a>를 확인하세요.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>부모 소득 기준을 생각하지 않고 신청</li>
<li>전입신고를 안 해 실거주 확인이 안 됨</li>
<li>계약서와 실제 월세 이체 금액이 다름</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>부모와 연락이 끊겼다면?</h3>
<p>원가구 소득 확인이 어려운 사정이 있으면 예외 심사가 가능할 수 있으니 주민센터에 상담하세요.</p>
<h3>지원 중 이사하면?</h3>
<p>변경 신고 후 새 계약 기준으로 다시 확인합니다. 신고하지 않으면 환수될 수 있습니다.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://www.bokjiro.go.kr" rel="noopener noreferrer" target="_blank">복지로</a> 모의계산·신청</li>
<li><a href="https://www.myhome.go.kr" rel="noopener noreferrer" target="_blank">마이홈포털</a> 청년 주거 지원 전체 보기</li>
<li>목돈 마련은 <a href="/youth-leap-account.html">청년도약계좌</a></li>
</ol>
""",
},
{
"file": "youth-leap-account.html",
"title": "청년도약계좌 조건과 만기 수령액 계산",
"desc": "청년도약계좌 가입 조건, 정부기여금 구조, 중도해지 시 불이익, 만기 수령액을 적금 계산기로 확인하는 방법을 정리했습니다.",
"search": "청년도약계좌 조건 만기 수령액 정부기여금 비과세 중도해지",
"related": [
("적금 이자 계산 방법", "/savings-interest.html"),
("청년내일저축계좌", "/youth-savings-account.html"),
("청년내일저축 자격", "/youth-savings-eligibility.html"),
("청년 월세 지원", "/youth-rent-support.html"),
],
"official": [
("서민금융진흥원", "https://www.kinfa.or.kr"),
("금융위원회", "https://www.fsc.go.kr"),
],
"hubs": ["savings-interest.html", "youth-savings-account.html", "youth-savings-eligibility.html"],
"intro": """<h1>청년도약계좌 조건과 만기 수령액 계산</h1>
<p>청년도약계좌는 5년 동안 매달 저축하면 <strong>정부기여금</strong>과 <strong>이자 비과세</strong> 혜택을 받는 상품입니다. 월 최대 70만 원까지 넣을 수 있어 목돈 마련용으로 관심이 높습니다.</p>
<p>하지만 5년은 깁니다. 가입 전에 “끝까지 넣을 수 있는 금액”을 정하는 것이 가장 중요합니다.</p>
<div class="tool-box">
<p><strong>만기 수령액 미리 계산</strong></p>
<p>월 납입액·금리·기간(60개월)을 넣어 이자를 확인해 보세요. 정부기여금은 별도로 더해 보세요.</p>
<p><a href="https://calculator.juho15.com/savings" rel="noopener noreferrer" target="_blank">금융계산기 — 적금 계산 열기</a></p>
</div>
""",
"rest": """<h2>가입 조건 체크</h2>
<ul>
<li>□ 만 19~34세 (병역 기간 일부 인정)</li>
<li>□ 개인소득 기준 이하</li>
<li>□ 가구소득 중위소득 일정 비율 이하</li>
</ul>
<p>가입 신청은 정해진 기간에 은행 앱으로 하고, 심사 후 개설됩니다. 기준은 <a href="https://www.kinfa.or.kr" rel="noopener noreferrer" target="_blank">서민금융진흥원</a> 공지를 확인하세요.</p>

<h2>수령액은 세 덩어리</h2>
<table>
<tr><th>구성</th><th>설명</th></tr>
<tr><td>원금</td><td>매달 넣은 금액 합계</td></tr>
<tr><td>은행 이자</td><td>적금 방식 이자, 비과세</td></tr>
<tr><td>정부기여금</td><td>소득 구간별로 납입액 일부 매칭</td></tr>
</table>
<p>적금 이자 계산 원리는 <a href="/savings-interest.html">적금 이자 계산 방법</a>에 정리했습니다. 예금보다 이자가 적어 보이는 이유도 거기서 확인할 수 있습니다.</p>

<h2>얼마를 넣어야 할까</h2>
<p>최대 70만 원을 무리하게 넣었다가 중간에 해지하면 혜택을 잃습니다. 생활비를 빼고 <strong>5년간 확실히 넣을 수 있는 금액</strong>으로 시작하고, 여유가 생기면 납입액을 늘리는 편이 안전합니다.</p>

<h2>청년내일저축계좌와 비교</h2>
<p>저소득 근로 청년이라면 <a href="/youth-savings-account.html">청년내일저축계좌</a>의 지원 비율이 더 클 수 있습니다. 중복 가입 제한이 있는지 반드시 확인하세요.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>정부기여금을 이자로 착각해 수령액을 과대 예상</li>
<li>납입 중단 기간이 길어져 기여금 미지급</li>
<li>특별중도해지 사유(결혼·출산 등)를 모르고 일반 해지</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>중간에 해지하면?</h3>
<p>일반 해지 시 정부기여금과 비과세 혜택이 사라질 수 있습니다. 특별중도해지 사유에 해당하는지 먼저 확인하세요.</p>
<h3>연말정산 공제가 되나요?</h3>
<p>소득공제 상품은 아닙니다. 연말정산 절세는 <a href="/year-end-preview.html">연말정산 미리보기</a>를 참고하세요.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://calculator.juho15.com/savings" rel="noopener noreferrer" target="_blank">적금 계산기</a>로 월 납입액 시뮬레이션</li>
<li><a href="https://www.kinfa.or.kr" rel="noopener noreferrer" target="_blank">서민금융진흥원</a> 가입 조건</li>
<li>사이트 내 <a href="/youth-savings-eligibility.html">청년내일저축 자격</a></li>
</ol>
""",
},
{
"file": "flu-vaccine-free.html",
"title": "독감 무료 예방접종 대상과 지정의료기관 찾기",
"desc": "인플루엔자 무료 예방접종 대상 연령, 접종 시기, 지정의료기관 조회와 준비물을 정리했습니다.",
"search": "독감 무료 예방접종 인플루엔자 대상 65세 어린이 임신부 지정의료기관",
"related": [
("국가건강검진 신청방법", "/medical-checkup.html"),
("건강검진 놓쳤을 때", "/medical-checkup-missed.html"),
("국가암검진 대상자 조회", "/cancer-screening.html"),
("실손보험 청구방법", "/insurance-claim.html"),
],
"official": [
("질병관리청 예방접종도우미", "https://nip.kdca.go.kr"),
("질병관리청", "https://www.kdca.go.kr"),
],
"hubs": ["medical-checkup.html", "medical-checkup-missed.html"],
"intro": """<h1>독감 무료 예방접종 대상과 지정의료기관 찾기</h1>
<p>찬바람이 불면 병원마다 독감 접종 안내문이 붙습니다. 그런데 <strong>무료 대상인데도 돈을 내고 맞는 경우</strong>가 생각보다 많습니다. 지정의료기관이 아닌 곳에서 맞았기 때문이죠.</p>
<p>우리 가족 중 누가 무료인지, 어디서 맞아야 하는지만 확인하면 됩니다.</p>
""",
"rest": """<h2>무료 접종 대상 (일반적 기준)</h2>
<table>
<tr><th>대상</th><th>비고</th></tr>
<tr><td>생후 6개월~13세 어린이</td><td>처음 맞는 9세 미만은 2회 접종</td></tr>
<tr><td>임신부</td><td>임신 주수 무관</td></tr>
<tr><td>65세 이상 어르신</td><td>연령별로 시작일이 다를 수 있음</td></tr>
</table>
<p>해마다 대상·시작일이 공지되니 <a href="https://nip.kdca.go.kr" rel="noopener noreferrer" target="_blank">예방접종도우미</a>에서 올해 기준을 확인하세요.</p>

<h2>접종 순서</h2>
<ol>
<li>예방접종도우미에서 <strong>지정의료기관</strong> 검색</li>
<li>병원에 전화해 백신 재고 확인 (초기에 몰림)</li>
<li>신분증(어린이는 보호자 확인 서류) 지참</li>
<li>접종 후 20~30분 병원에 머물며 이상반응 관찰</li>
</ol>

<h2>언제 맞는 게 좋을까</h2>
<p>보통 10월~11월에 맞으면 유행기 전에 항체가 생깁니다. 유행이 시작된 뒤에도 접종은 도움이 되니 늦었다고 포기하지 마세요.</p>

<h2>함께 챙기면 좋은 것</h2>
<ul>
<li>올해 <a href="/medical-checkup.html">국가건강검진</a> 대상인데 아직 안 받았다면 연말 전에 함께 예약</li>
<li>놓친 검진은 <a href="/medical-checkup-missed.html">추가 검진 방법</a> 참고</li>
<li>65세 이상은 폐렴구균 접종 이력도 확인</li>
</ul>

<h2>자주 하는 실수</h2>
<ul>
<li>지정의료기관이 아닌 곳에서 맞아 비용 지불</li>
<li>9세 미만 첫 접종 아이의 2차 접종을 잊음</li>
<li>열이 있는 날 무리하게 접종</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>코로나 백신과 같이 맞아도 되나요?</h3>
<p>동시 접종이 가능하다고 안내되는 경우가 많지만, 해당 시즌 지침과 의사 판단을 따르세요.</p>
<h3>유료 대상은 얼마인가요?</h3>
<p>병원마다 다르며 보통 수만 원 선입니다. 지자체에 따라 추가 무료 대상을 두기도 합니다.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://nip.kdca.go.kr" rel="noopener noreferrer" target="_blank">예방접종도우미</a> 지정의료기관 찾기</li>
<li>사이트 내 <a href="/medical-checkup.html">국가건강검진</a></li>
<li><a href="/cancer-screening.html">국가암검진 대상자 조회</a></li>
</ol>
""",
},
{
"file": "emergency-welfare.html",
"title": "긴급복지지원 신청 대상과 생계비 지원 받는 법",
"desc": "실직·질병·화재 등 갑작스러운 위기 때 받을 수 있는 긴급복지지원의 대상, 지원 종류, 129 상담 신청 순서를 정리했습니다.",
"search": "긴급복지지원 생계비 긴급지원 129 위기 실직 의료비",
"related": [
("기초생활수급자 혜택과 신청", "/basic-livelihood.html"),
("차상위계층 신청 방법", "/near-poor-application.html"),
("실업급여 신청방법", "/unemployment-benefit.html"),
("겨울철 난방비 지원", "/heating-cost-support.html"),
],
"official": [
("복지로", "https://www.bokjiro.go.kr"),
("보건복지부", "https://www.mohw.go.kr"),
],
"hubs": ["basic-livelihood.html", "near-poor-application.html"],
"intro": """<h1>긴급복지지원 신청 대상과 생계비 지원 받는 법</h1>
<p>갑자기 일자리를 잃었거나 큰 병에 걸렸을 때, 기초수급 심사를 기다릴 여유가 없을 수 있습니다. <strong>긴급복지지원</strong>은 이런 위기 상황에서 <strong>먼저 지원하고 나중에 확인하는</strong> 제도입니다.</p>
<p>“나도 해당될까?” 싶다면 고민하지 말고 129에 전화하는 것이 첫걸음입니다.</p>
""",
"rest": """<h2>이런 위기 상황이 대상</h2>
<ul>
<li>주 소득자의 사망·가출·행방불명·구금</li>
<li>중한 질병·부상</li>
<li>실직·휴폐업 등으로 소득 상실</li>
<li>화재 등으로 거주가 곤란해진 경우</li>
<li>가정폭력, 방임 등</li>
</ul>

<h2>지원 종류</h2>
<table>
<tr><th>종류</th><th>내용</th></tr>
<tr><td>생계지원</td><td>가구원 수에 따른 생계비 (원칙 1개월, 연장 가능)</td></tr>
<tr><td>의료지원</td><td>검사·치료비 일정 한도</td></tr>
<tr><td>주거지원</td><td>임시 거소 제공</td></tr>
<tr><td>기타</td><td>동절기 연료비, 해산·장제비, 전기요금 등</td></tr>
</table>

<h2>신청 순서</h2>
<ol>
<li><strong>129</strong>(보건복지상담센터) 또는 시·군·구청, 주민센터에 연락</li>
<li>담당 공무원 현장 확인</li>
<li>긴급성이 인정되면 <strong>먼저 지원</strong></li>
<li>이후 소득·재산 사후 조사</li>
</ol>
<p>이웃이 위기에 처한 것을 알게 되었다면 본인 대신 신고할 수도 있습니다.</p>

<h2>그 다음 단계</h2>
<p>긴급지원은 단기 지원입니다. 상황이 길어질 것 같다면 <a href="/basic-livelihood.html">기초생활수급</a>이나 <a href="/near-poor-application.html">차상위계층</a> 신청을 함께 상담하세요. 실직이라면 <a href="/unemployment-benefit.html">실업급여</a>도 바로 알아봐야 합니다.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>“재산이 조금 있어서 안 되겠지” 하고 상담조차 안 함</li>
<li>사후 조사에서 허위 사실이 드러나 환수</li>
<li>긴급지원만 받고 장기 지원 신청을 놓침</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>지원은 얼마나 빨리 나오나요?</h3>
<p>긴급성이 인정되면 신청 후 짧은 기간 안에 지원이 결정되는 것이 원칙입니다.</p>
<h3>같은 이유로 다시 받을 수 있나요?</h3>
<p>동일 위기 사유로는 일정 기간 재지원이 제한될 수 있습니다.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li>보건복지상담센터 <strong>129</strong></li>
<li><a href="https://www.bokjiro.go.kr" rel="noopener noreferrer" target="_blank">복지로</a> 긴급지원 안내</li>
<li>겨울철이라면 <a href="/heating-cost-support.html">난방비 지원</a>도 확인</li>
</ol>
""",
},
{
"file": "naeil-learning-card.html",
"title": "국민내일배움카드 발급 조건과 훈련비 지원 사용법",
"desc": "국민내일배움카드 발급 대상, 지원 한도, 고용24 신청 순서, 수강 과정 고르는 요령과 자부담 비율을 정리했습니다.",
"search": "국민내일배움카드 내일배움카드 발급 훈련비 고용24 국비지원",
"related": [
("실업급여 신청방법", "/unemployment-benefit.html"),
("실업급여 수급 중 재취업", "/unemployment-early-reemploy.html"),
("고용보험 가입이력 조회", "/employment-insurance.html"),
("노인일자리 신청방법", "/senior-job.html"),
],
"official": [
("고용24", "https://www.work24.go.kr"),
("고용노동부", "https://www.moel.go.kr"),
],
"hubs": ["unemployment-benefit.html", "unemployment-early-reemploy.html"],
"intro": """<h1>국민내일배움카드 발급 조건과 훈련비 지원 사용법</h1>
<p>자격증 공부나 직무 교육을 하고 싶은데 학원비가 부담된다면 <strong>국민내일배움카드</strong>부터 확인하세요. 5년간 일정 한도의 훈련비를 지원받을 수 있습니다.</p>
<p>재직자, 구직자, 자영업자 등 대부분 발급 대상이고, 일부 예외만 확인하면 됩니다.</p>
""",
"rest": """<h2>발급 대상과 예외</h2>
<ul>
<li>대상: 구직자, 재직자, 자영업자 등 대부분의 국민</li>
<li>예외: 공무원·사립학교 교직원, 일정 소득 이상 대규모 기업 재직자·자영업자 등</li>
</ul>

<h2>발급 순서</h2>
<ol>
<li><a href="https://www.work24.go.kr" rel="noopener noreferrer" target="_blank">고용24</a>에서 카드 발급 신청</li>
<li>구직자는 온라인 사전 동영상 시청 등 절차 이수</li>
<li>승인 후 카드사에서 카드 발급</li>
<li>고용24에서 훈련 과정 검색·수강 신청</li>
</ol>

<h2>지원 한도와 자부담</h2>
<table>
<tr><th>항목</th><th>내용</th></tr>
<tr><td>지원 한도</td><td>5년간 300만~500만 원 수준 (대상별 상이)</td></tr>
<tr><td>자부담</td><td>과정·대상에 따라 일정 비율 본인 부담</td></tr>
<tr><td>훈련장려금</td><td>구직자가 일정 출석 시 지급되는 경우 있음</td></tr>
</table>
<p>실업급여 수급자라면 훈련 참여가 구직활동으로 인정될 수 있습니다. <a href="/unemployment-benefit.html">실업급여 가이드</a>를 함께 보세요.</p>

<h2>과정 고르는 요령</h2>
<ul>
<li>훈련기관 평가 등급·취업률 확인</li>
<li>국가기간·전략산업 직종훈련은 자부담이 낮은 편</li>
<li>온라인 과정은 수료 기준(진도율·시험) 확인</li>
</ul>

<h2>자주 하는 실수</h2>
<ul>
<li>출석률 미달로 수료 실패 → 자부담 증가·제재</li>
<li>한도를 짧은 과정에 다 써 버림</li>
<li>재취업 후 카드 상태 변경을 확인하지 않음</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>퇴사 후 실업급여 받으면서도 쓸 수 있나요?</h3>
<p>가능합니다. 출석 요건만 지키면 되고, 재취업하면 <a href="/unemployment-early-reemploy.html">조기취업수당</a>도 확인하세요.</p>
<h3>카드 유효기간은?</h3>
<p>발급일로부터 5년이며, 이후 재발급 기준을 확인하세요.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://www.work24.go.kr" rel="noopener noreferrer" target="_blank">고용24</a> 카드 신청·과정 검색</li>
<li>사이트 내 <a href="/employment-insurance.html">고용보험 가입이력</a></li>
<li><a href="/unemployment-benefit.html">실업급여 신청 총정리</a></li>
</ol>
""",
},
{
"file": "kpass-transport-refund.html",
"title": "K-패스 교통비 환급 조건과 가입 방법",
"desc": "K-패스 대중교통비 환급 비율, 월 이용 횟수 조건, 카드 발급과 회원가입 순서, 연말정산 대중교통 공제와의 관계를 정리했습니다.",
"search": "K패스 케이패스 교통비 환급 대중교통 알뜰교통카드 청년 저소득",
"related": [
("연말정산 미리보기", "/year-end-preview.html"),
("연말정산 환급 체크리스트", "/year-end-refund-tips.html"),
("통신비 감면 신청방법", "/telecom-discount.html"),
("신용점수 조회방법", "/credit-score.html"),
],
"official": [
("K-패스", "https://korea-pass.kr"),
("국토교통부", "https://www.molit.go.kr"),
],
"hubs": ["telecom-discount.html", "year-end-refund-tips.html"],
"intro": """<h1>K-패스 교통비 환급 조건과 가입 방법</h1>
<p>매일 버스·지하철을 탄다면 <strong>K-패스</strong>를 안 쓰는 것만으로 매달 수만 원을 놓칠 수 있습니다. 쓴 교통비의 일정 비율을 다음 달에 돌려받는 제도입니다.</p>
<p>카드만 만들고 <strong>회원가입을 안 해서</strong> 환급을 못 받는 경우가 가장 흔합니다. 순서를 지키는 것이 핵심입니다.</p>
""",
"rest": """<h2>환급 비율 (기본 구조)</h2>
<table>
<tr><th>대상</th><th>환급률</th></tr>
<tr><td>일반</td><td>20%</td></tr>
<tr><td>청년(만 19~34세)</td><td>30%</td></tr>
<tr><td>저소득층</td><td>53.3%</td></tr>
</table>
<p>월 15회 이상 이용해야 하고, 환급 횟수에는 상한이 있습니다. 다자녀·어르신 추가 혜택이나 정액형 등 개편 내용은 <a href="https://korea-pass.kr" rel="noopener noreferrer" target="_blank">K-패스 누리집</a>에서 최신 기준을 확인하세요.</p>

<h2>가입 순서</h2>
<ol>
<li>K-패스 제휴 카드사에서 카드 발급 (신용·체크)</li>
<li><strong>K-패스 앱·누리집에서 회원가입 후 카드 등록</strong></li>
<li>다음 달부터 이용 실적에 따라 환급</li>
</ol>

<h2>나에게 맞는 카드 고르기</h2>
<ul>
<li>체크카드: 연말정산 공제율이 높고 과소비 방지</li>
<li>신용카드: 카드사 자체 할인 혜택이 더해질 수 있음</li>
<li>기존 알뜰교통카드 이용자는 전환 절차 확인</li>
</ul>

<h2>연말정산과 같이 챙기기</h2>
<p>대중교통 사용분은 연말정산에서 별도 공제율이 적용됩니다. K-패스로 환급도 받고 공제도 챙기면 두 번 이득입니다. 남은 기간 결제 전략은 <a href="/year-end-preview.html">연말정산 미리보기</a>를 참고하세요.</p>

<h2>자주 하는 실수</h2>
<ul>
<li>카드 발급 후 회원가입·카드 등록 누락</li>
<li>월 15회 미만이라 환급 0원</li>
<li>청년·저소득 증빙 등록을 안 해 일반 비율 적용</li>
</ul>

<h2>자주 묻는 질문</h2>
<h3>고속버스·KTX도 되나요?</h3>
<p>대상은 시내·광역버스, 지하철 등 대중교통 위주이며 일부 교통수단은 제외됩니다.</p>
<h3>환급은 언제 들어오나요?</h3>
<p>이용 다음 달에 카드 결제 대금 차감 또는 포인트 등 카드사 방식으로 지급됩니다.</p>

<h2>다음에 확인할 링크</h2>
<ol>
<li><a href="https://korea-pass.kr" rel="noopener noreferrer" target="_blank">K-패스</a> 회원가입·카드 등록</li>
<li>사이트 내 <a href="/year-end-refund-tips.html">연말정산 체크리스트</a></li>
<li>고정비 절약은 <a href="/telecom-discount.html">통신비 감면</a>도 확인</li>
</ol>
""",
},
]


def update_sitemap(path):
    xml = path.read_text(encoding="utf-8")
    added = ""
    for a in ARTICLES:
        loc = f"{SITE}/{a['file']}"
        if loc in xml:
            continue
        added += (f"  <url><loc>{loc}</loc><lastmod>{LASTMOD}</lastmod>"
                  f"<changefreq>monthly</changefreq><priority>0.85</priority></url>\n")
    xml = xml.replace("</urlset>", added + "</urlset>")
    xml = re.sub(r"(<loc>https://www\.juho15\.com/</loc><lastmod>)[^<]+", rf"\g<1>{LASTMOD}", xml)
    path.write_text(xml, encoding="utf-8")


def update_search(path):
    js = path.read_text(encoding="utf-8")
    anchor = "const articles = ["
    if anchor not in js:
        anchor = "articles = ["
    entries = ""
    for a in ARTICLES:
        url = f"/{a['file']}"
        if url in js:
            continue
        entries += f'\n    {{ title: "{a["title"]}", url: "{url}", keywords: "{a["search"]}" }},'
    js = js.replace(anchor, anchor + entries, 1)
    path.write_text(js, encoding="utf-8")


def main():
    for a in ARTICLES:
        (ROOT / a["file"]).write_text(base.build_page(a), encoding="utf-8")
        print(f"created: {a['file']}")
    for a in ARTICLES:
        for hub in a["hubs"]:
            base.patch_related(hub, [(a["title"], f"/{a['file']}")])
    update_sitemap(ROOT / "sitemap.xml")
    update_sitemap(ROOT / "sitemaps" / "main.xml")
    update_search(ROOT / "js" / "search.js")


if __name__ == "__main__":
    main()
