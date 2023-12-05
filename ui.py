import streamlit as st
from main import *
import json

if "topic" not in st.session_state:
    st.session_state.i = 0
    st.session_state.topic = ""
    st.session_state.y = 5
    st.session_state.t = False

with st.sidebar:
    formInPut = st.form("input")
    formInPut.header("MCQ Generator")
    formInPut.write("Generate multiple-choice question for any topic")
    st.session_state.topic = st.text_input("Enter a topic")
    st.session_state.y = st.number_input(label="Number of question ", value=None, placeholder="Type a number...")
    container = st.container(border=True)
    submitted = formInPut.form_submit_button("Generate")

if submitted:
    st.session_state.t = True
if st.session_state.t:
    form2 = st.form("output", clear_on_submit=False)
    with st.spinner("Generating...."):
        questions = creatQuestions(st.session_state.topic, str(st.session_state.y))
        l = json.loads(questions)

    submitted2 = form2.form_submit_button("submit")

    for i in l:
        ri = form2.radio(l[i]["question"], (l[i])["answers"], index=None, disabled=False)

        if submitted2:
            form2.write("the answer is " + l[i]["answer"])
            if ri == l[i]["answer"]:
                st.session_state.i += 1
            elif ri != l[i]["answer"] and ri != None:
                pass
    container.write("you scored " + str(st.session_state.i) + " out of " + str(st.session_state.y))
