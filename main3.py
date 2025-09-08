import streamlit as st
from ai_agents import generate_test_steps, explain_results
from selenium_runner import run_test

st.title("🤖 AI Website Tester")
st.write("Type a natural instruction, and this AI agent will test a website for you!")

user_input = st.text_area(
    "Enter your test instruction:",
    "Test login on https://the-internet.herokuapp.com/login with username 'tomsmith' and password 'SuperSecretPassword!'"
)

if st.button("Run Test"):
    with st.spinner("Generating test steps..."):
        steps_json = generate_test_steps(user_input)

    with st.spinner("Running test in browser..."):
        results = run_test(steps_json)

    st.session_state["steps_json"] = steps_json
    st.session_state["results"] = results

if "steps_json" in st.session_state:
    st.subheader("📝 Generated Steps (AI)")
    st.code(st.session_state["steps_json"], language="json")

if "results" in st.session_state:
    st.subheader("✅ Test Results")
    for r in st.session_state["results"]:
        st.write(r)

    st.subheader("💬 Ask about the results")
    followup_question = st.text_input("Enter a follow-up question (e.g., 'Why did it fail?')")

    if st.button("Explain") and followup_question.strip():
        explanation = explain_results(st.session_state["results"], followup_question)
        st.markdown("### 🤖 AI Explanation")
        st.write(explanation)
