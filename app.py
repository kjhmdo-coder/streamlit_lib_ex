import time
import pandas as pd
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Streamlit 핵심 UI 위젯 가이드",
    page_icon="🎨",
    layout="wide",
)

# 상단 안내 배너
st.title("🎨 Streamlit 핵심 UI 위젯 및 사용 방법 안내")
st.info(
    "👋 **학생 여러분을 위한 안내:** 이 웹앱은 파이썬 **Streamlit**으로 만들 수 있는 주요 UI 위젯들을 직접 눌러보고 체험할 수 있는 가이드입니다.\n\n"
    "1. 위쪽 **탭(1~4번)**을 눌러 입력창, 레이아웃, 차트, 챗봇, 알림 효과를 직접 테스트해 보세요.\n"
    "2. 각 화면 아래의 **`📋 파이썬 코드 보기`**를 펼치면 내 앱에 바로 복사해 쓸 수 있는 코드와 위젯 함수명(`st.xxx`)을 확인할 수 있습니다.\n"
    "3. **`💡 바이브 코딩 프롬프트 모음`** 탭에서 AI에게 요청할 프롬프트 양식을 복사해 활용해 보세요."
)

# ---------------------------------------------------------
# 사이드바 (Sidebar) - 예제 1-2의 사이드바 포함
# ---------------------------------------------------------
with st.sidebar:
    st.header("설정 메뉴")
    user_grade = st.selectbox("학년 선택", ["1학년", "2학년", "3학년"])
    st.caption(f"현재 선택된 학년: **{user_grade}** (`st.sidebar` + `st.selectbox`)")

    st.divider()
    st.subheader("💡 바이브 코딩 팁")
    st.markdown(
        "AI에게 코드를 요청할 때 **위젯 함수명**을 직접 적어주면 훨씬 정확한 화면이 만들어집니다.\n\n"
        "- **구역 나누기:** `st.sidebar`, `st.tabs`, `st.columns`\n"
        "- **입력 받기:** `st.text_input`, `st.slider`, `st.selectbox`\n"
        "- **결과 보여주기:** `st.metric`, `st.bar_chart`, `st.dataframe`"
    )

# ---------------------------------------------------------
# 메인 화면 5개 탭 구성
# ---------------------------------------------------------
main_tab1, main_tab2, main_tab3, main_tab4, main_tab5 = st.tabs([
    "1️⃣ 입력 및 선택 위젯",
    "2️⃣ 화면 배치 및 레이아웃",
    "3️⃣ 데이터·차트 및 챗봇 UI",
    "4️⃣ 알림 및 진행 상태",
    "💡 바이브 코딩 프롬프트 모음",
])

# =========================================================
# TAB 1: 입력 및 선택 위젯 (예제 1-1)
# =========================================================
with main_tab1:
    st.header("1-1. 입력 및 선택 위젯 (Input & Selection)")
    st.write("사용자로부터 텍스트, 숫자, 선택지 등을 입력받아 변수에 저장할 때 사용합니다.")

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("📝 텍스트 & 숫자 입력")
        st.caption("`st.text_input` / `st.text_area` / `st.slider`")
        name = st.text_input("이름을 입력하세요", placeholder="예: 홍길동")
        memo = st.text_area("오늘의 다짐", height=100, placeholder="자유롭게 입력해 보세요.")
        score = st.slider("목표 점수 선택", min_value=0, max_value=100, value=80, step=5)

    with col_right:
        st.subheader("🔘 선택 및 토글 위젯")
        st.caption("`st.selectbox` / `st.multiselect` / `st.segmented_control` / `st.toggle`")
        subject = st.selectbox("가장 좋아하는 과목", ["정보", "수학", "과학", "국어", "영어"])
        tags = st.multiselect("관심 분야 (복수 선택)", ["AI", "데이터분석", "게임제작", "웹개발"])
        mode = st.segmented_control("화면 모드", ["간단히 보기", "자세히 보기"], default="간단히 보기")
        agree = st.toggle("알림 받기 활성화", value=True)

    st.divider()
    st.subheader("🖱️ 실행 버튼 & 파일 다운로드")
    st.caption("`st.button` / `st.download_button`")

    btn_col1, btn_col2 = st.columns([1, 2])
    with btn_col1:
        if st.button("결과 확인하기", type="primary"):
            display_name = name if name else "학생"
            st.success(f"{display_name}님의 {subject} 목표 점수는 {score}점입니다! (모드: {mode}, 알림: {'ON' if agree else 'OFF'})")
            if tags:
                st.write("선택한 관심 분야:", ", ".join(tags))
            if memo:
                st.write("오늘의 다짐:", memo)

    with btn_col2:
        st.download_button(
            label="결과 텍스트 다운로드",
            data=f"이름: {name}\n과목: {subject}\n목표점수: {score}\n관심분야: {tags}\n다짐: {memo}",
            file_name="my_goal.txt",
        )

    with st.expander("📋 [예제 1-1] 파이썬 코드 보기 & 복사"):
        st.code(
            """import streamlit as st

# 1. 텍스트 & 숫자 입력
name = st.text_input("이름을 입력하세요", placeholder="예: 홍길동")
memo = st.text_area("오늘의 다짐", height=100)
score = st.slider("목표 점수 선택", min_value=0, max_value=100, value=80, step=5)

# 2. 선택 위젯
subject = st.selectbox("가장 좋아하는 과목", ["정보", "수학", "과학", "국어", "영어"])
tags = st.multiselect("관심 분야 (복수 선택)", ["AI", "데이터분석", "게임제작", "웹개발"])
mode = st.segmented_control("화면 모드", ["간단히 보기", "자세히 보기"], default="간단히 보기")
agree = st.toggle("알림 받기 활성화", value=True)

# 3. 버튼 & 다운로드
if st.button("결과 확인하기", type="primary"):
    st.write(f"{name}님의 {subject} 목표 점수는 {score}점입니다!")

st.download_button(
    label="결과 텍스트 다운로드",
    data=f"이름: {name}\n과목: {subject}\n목표점수: {score}",
    file_name="my_goal.txt"
)""",
            language="python",
        )

# =========================================================
# TAB 2: 화면 배치 및 레이아웃 (예제 1-2)
# =========================================================
with main_tab2:
    st.header("1-2. 화면 배치 및 레이아웃 (Layout & Containers)")
    st.write("`st.tabs`, `st.columns`, `st.form`, `st.expander`를 사용해 웹페이지처럼 구역을 나눌 수 있습니다.")

    # 예제 1-2의 내부 탭 나누기
    sub_tab1, sub_tab2 = st.tabs(["📊 메인 화면", "ℹ️ 도움말"])

    with sub_tab1:
        st.caption("가로 2단 분할 (`st.columns(2)`)")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("왼쪽 구역")
            st.info("여기에 입력 위젯을 배치할 수 있습니다.")
        with col2:
            st.subheader("오른쪽 구역")
            st.success("여기에 결과 화면을 배치할 수 있습니다.")

        st.divider()
        st.caption("한 번에 묶어서 제출하는 폼 (`st.form`) - 입력할 때마다 화면이 새로고침되는 것을 방지합니다.")
        with st.form("survey_form"):
            q1 = st.text_input("질문 1: 오늘 기분은 어떤가요?")
            q2 = st.slider("질문 2: 수업 만족도 (1~5)", 1, 5, 5)
            submitted = st.form_submit_button("한 번에 제출하기")
            if submitted:
                st.write("제출 완료:", q1 if q1 else "(미입력)", f"/ 만족도: {q2}점")

    with sub_tab2:
        st.caption("접이식 상자 (`st.expander`)")
        with st.expander("사용 방법을 보려면 클릭하세요", expanded=True):
            st.write("왼쪽 사이드바(`st.sidebar`)에서 학년을 고른 뒤 설문을 작성해 주세요.")

    with st.expander("📋 [예제 1-2] 파이썬 코드 보기 & 복사"):
        st.code(
            """import streamlit as st

# 1. 왼쪽 사이드바 메뉴
with st.sidebar:
    st.header("설정 메뉴")
    user_grade = st.selectbox("학년 선택", ["1학년", "2학년", "3학년"])

# 2. 상단 탭 나누기
tab1, tab2 = st.tabs(["📊 메인 화면", "ℹ️ 도움말"])

with tab1:
    # 3. 가로 2단 분할 (좌우 배치)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("왼쪽 구역")
        st.info("여기에 입력 위젯을 배치할 수 있습니다.")
    with col2:
        st.subheader("오른쪽 구역")
        st.success("여기에 결과 화면을 배치할 수 있습니다.")

    # 4. 한 번에 제출하는 폼(Form)
    with st.form("survey_form"):
        q1 = st.text_input("질문 1: 오늘 기분은 어떤가요?")
        q2 = st.slider("질문 2: 수업 만족도 (1~5)", 1, 5, 5)
        submitted = st.form_submit_button("한 번에 제출하기")
        if submitted:
            st.write("제출 완료:", q1, q2)

with tab2:
    # 5. 접이식 상자(Expander)
    with st.expander("사용 방법을 보려면 클릭하세요"):
        st.write("왼쪽 사이드바에서 학년을 고른 뒤 설문을 작성해 주세요.")""",
            language="python",
        )

# =========================================================
# TAB 3: 데이터·차트 및 챗봇 UI (예제 1-3)
# =========================================================
with main_tab3:
    st.header("1-3. 데이터·차트 및 챗봇 UI (Data, Charts & Chat)")

    st.subheader("1) 핵심 숫자 강조 카드 (`st.metric`)")
    c1, c2, c3 = st.columns(3)
    c1.metric("평균 점수", "88.5점", "+4.2점")
    c2.metric("달성률", "92%", "+10%")
    c3.metric("남은 기간", "D-14", "-1일")

    st.divider()
    st.subheader("2) 직접 수정 가능한 표 & 막대 차트 (`st.data_editor` + `st.bar_chart`)")
    st.caption("표의 점수를 더블클릭해 직접 수정하거나 아래 `+` 행을 추가하면 오른쪽 막대 차트가 실시간으로 바뀝니다!")

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        df = pd.DataFrame({
            "과목": ["국어", "수학", "영어", "정보"],
            "점수": [85, 90, 80, 95],
        })
        edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

    with chart_col2:
        valid_df = edited_df.dropna(subset=["과목"])
        if not valid_df.empty:
            st.bar_chart(valid_df.set_index("과목"))

    st.divider()
    st.subheader("3) 말풍선 챗봇 UI (`st.chat_message` + `st.chat_input`)")
    if "demo_chat" not in st.session_state:
        st.session_state.demo_chat = [
            {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요? 아래 입력창에 메시지를 적어보세요."}
        ]

    for msg in st.session_state.demo_chat:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_msg = st.chat_input("메시지를 입력하세요...")
    if user_msg:
        st.session_state.demo_chat.append({"role": "user", "content": user_msg})
        reply = f"'{user_msg}'에 대한 답변입니다!"
        st.session_state.demo_chat.append({"role": "assistant", "content": reply})
        st.rerun()

    with st.expander("📋 [예제 1-3] 파이썬 코드 보기 & 복사"):
        st.code(
            """import streamlit as st
import pandas as pd

# 1. 핵심 숫자 강조 카드 (Metric)
c1, c2, c3 = st.columns(3)
c1.metric("평균 점수", "88.5점", "+4.2점")
c2.metric("달성률", "92%", "+10%")
c3.metric("남은 기간", "D-14", "-1일")

# 2. 직접 수정 가능한 표 & 막대 차트
df = pd.DataFrame({
    "과목": ["국어", "수학", "영어", "정보"],
    "점수": [85, 90, 80, 95]
})
edited_df = st.data_editor(df, num_rows="dynamic")  # 표 값을 직접 수정 가능
st.bar_chart(edited_df.set_index("과목"))

# 3. 말풍선 챗봇 UI 예시
with st.chat_message("assistant"):
    st.write("안녕하세요! 무엇을 도와드릴까요?")

user_msg = st.chat_input("메시지를 입력하세요...")
if user_msg:
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant"):
        st.write(f"'{user_msg}'에 대한 답변입니다!")""",
            language="python",
        )

# =========================================================
# TAB 4: 알림 및 진행 상태 (예제 1-4)
# =========================================================
with main_tab4:
    st.header("1-4. 알림 및 진행 상태 (Status & Feedback)")

    st.subheader("1) 4가지 색상 알림 박스")
    a1, a2 = st.columns(2)
    with a1:
        st.info("`st.info`: 안내 문구를 표시할 때 사용합니다.")
        st.success("`st.success`: 작업 완료나 정답을 알릴 때 사용합니다.")
    with a2:
        st.warning("`st.warning`: 주의사항이나 경고를 표시할 때 사용합니다.")
        st.error("`st.error`: 오류나 오답을 표시할 때 사용합니다.")

    st.divider()
    st.subheader("2) 로딩 스피너, 토스트 알림 & 풍선 축하 효과")
    st.info("안내: 아래 버튼을 눌러 진행 효과를 테스트해 보세요.")

    if st.button("미션 완료 테스트", type="primary"):
        with st.spinner("결과를 계산하는 중입니다..."):
            time.sleep(1)
        st.toast("저장 완료!", icon="✅")
        st.success("축하합니다! 모든 미션을 완료했습니다.")
        st.balloons()

    with st.expander("📋 [예제 1-4] 파이썬 코드 보기 & 복사"):
        st.code(
            """import streamlit as st
import time

st.info("안내: 아래 버튼을 눌러 진행 효과를 테스트해 보세요.")

if st.button("미션 완료 테스트"):
    with st.spinner("결과를 계산하는 중입니다..."):
        time.sleep(1)
    st.toast("저장 완료!", icon="✅")
    st.success("축하합니다! 모든 미션을 완료했습니다.")
    st.balloons()""",
            language="python",
        )

# =========================================================
# TAB 5: 바이브 코딩 프롬프트 모음
# =========================================================
with main_tab5:
    st.header("💡 만능 바이브 코딩 프롬프트 공식 & 템플릿")
    st.markdown(
        "> **[만능 프롬프트 공식]**  \n"
        "> **① 앱 주제 및 목적** + **② 화면 레이아웃(`st.sidebar`, `st.tabs`, `st.columns`)** + **③ 입력 위젯** + **④ 출력·차트 및 피드백 위젯**"
    )

    st.subheader("템플릿 1. 학습 플래너 & 디데이·성적 대시보드")
    st.code(
        """파이썬 Streamlit으로 [시험 대비 나만의 학습 플래너 & 성적 분석기] 웹앱을 만들어줘.
1. 화면 구성: 왼쪽 st.sidebar에는 시험 날짜를 고르는 st.date_input과 목표 평균 점수를 정하는 st.slider를 배치해줘.
2. 메인 상단: 오늘 날짜 기준으로 남은 D-Day와 현재 평균 점수, 목표 점수와의 차이를 st.metric 3개로 나란히(st.columns) 보여줘.
3. 데이터 입력 및 시각화: st.data_editor를 사용해 사용자가 직접 과목명, 내 점수, 목표 점수를 표에서 수정하고 행을 추가할 수 있게 해줘. 표 아래에는 과목별 점수를 비교하는 st.bar_chart를 자동으로 그려줘.
4. 피드백: 평균 점수가 목표 점수를 넘으면 st.success 메시지와 함께 st.balloons() 축하 효과를 띄워줘.""",
        language="text",
    )

    st.subheader("템플릿 2. 고민 상담 & 스무고개 챗봇 UI")
    st.code(
        """파이썬 Streamlit으로 [학교 생활 고민을 들어주는 다정한 선배 챗봇] 웹앱을 만들어줘. (외부 API 키 없이 규칙 기반 응답으로 작동하게 작성해줘)
1. 대화 유지: st.session_state를 사용해서 새로고침되어도 이전 대화 내역이 화면에 계속 남아있게 해줘.
2. 채팅 UI: st.chat_message("assistant")와 st.chat_message("user")를 사용해 실제 메신저처럼 말풍선으로 대화가 이어지게 만들고, 화면 맨 아래 st.chat_input으로 메시지를 입력받게 해줘.
3. 편의 기능: 왼쪽 st.sidebar에는 '대화 내용 초기화' 버튼(st.button)과 자주 묻는 질문 예시 버튼 3개를 만들어서, 버튼을 누르면 바로 질문이 입력되도록 해줘.""",
        language="text",
    )

    st.subheader("템플릿 3. 우리 반 설문조사 & 실시간 통계 분석기")
    st.code(
        """파이썬 Streamlit으로 [우리 반 점심 메뉴 및 급식 만족도 실시간 설문조사] 웹앱을 만들어줘.
1. 설문 입력 폼: st.form을 사용해서 응답자 이름(st.text_input), 선호 메뉴 선택(st.pills), 급식 만족도 별점(st.feedback("stars")), 건의사항(st.text_area)을 입력받고 '설문 제출' 버튼을 누를 때만 데이터가 저장(st.session_state)되게 해줘.
2. 제출 알림: 제출 버튼을 누르면 화면 우측 하단에 st.toast("소중한 의견 감사합니다!") 알림을 띄워줘.
3. 실시간 결과 탭: st.tabs로 '실시간 통계 차트' 탭과 '전체 응답 데이터' 탭을 나누고, 차트 탭에는 메뉴별 득표수를 st.bar_chart로, 데이터 탭에는 누적된 표(st.dataframe)와 CSV 파일 다운로드 버튼(st.download_button)을 넣어줘.""",
        language="text",
    )
