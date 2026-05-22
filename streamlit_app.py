import random
import streamlit as st

st.title("🧮 사칙 연산 계산 연습")
st.write("아래 문제를 풀어보세요. +, -, ×, ÷ 연산을 선택하고 문제를 생성합니다.")

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,    
    "×": lambda a, b: a * b,
    "÷": lambda a, b: a // b if b != 0 and a % b == 0 else None,
}

operator = st.selectbox("연산 선택", ["+", "-", "×", "÷"])
difficulty = st.radio("난이도", ["쉬움", "보통", "어려움"])

if difficulty == "쉬움":
    min_val, max_val = 1, 20
elif difficulty == "보통":
    min_val, max_val = 1, 50
else:
    min_val, max_val = 1, 100

if st.button("새 문제 생성"):
    a = random.randint(min_val, max_val)
    b = random.randint(min_val, max_val)
    if operator == "÷":
        b = random.randint(min_val, max_val)
        while b == 0 or a % b != 0:
            a = random.randint(min_val, max_val)
            b = random.randint(min_val, max_val)

    st.session_state.question = f"{a} {operator} {b} = ?"
    st.session_state.answer = operators[operator](a, b)

if "question" not in st.session_state:
    st.session_state.question = ""
    st.session_state.answer = None

if st.session_state.question:
    st.subheader("문제")
    st.write(st.session_state.question)
    user_answer = st.text_input("정답을 입력하세요", key="user_answer")
    if st.button("채점"):
        try:
            user_value = int(user_answer)
            if user_value == st.session_state.answer:
                st.success("정답입니다! 🎉")
            else:
                st.error(f"틀렸습니다. 정답은 {st.session_state.answer} 입니다.")
        except ValueError:
            st.warning("숫자를 입력해 주세요.")

st.write("---")
st.write("### 사용 방법")
st.write("1. 연산과 난이도를 선택합니다.\n2. 새 문제 생성을 누릅니다.\n3. 정답을 입력하고 채점을 눌러 확인합니다.")
