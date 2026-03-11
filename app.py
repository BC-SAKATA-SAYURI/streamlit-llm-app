from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import streamlit as st

st.title("教えて！専門家さん")

st.write("##### 動作モード1: 教育の専門家")
st.write("教育の専門家に相談できます")
st.write("##### 動作モード2: 健康の専門家")
st.write("健康の専門家に相談できます")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["教育の専門家", "健康の専門家"]
)

st.divider()

if selected_item == "教育の専門家":
    st.write("教育の専門家に相談したいことを入力してください")
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    message = [
    SystemMessage(content="あなたは教育の専門家です。"),
    HumanMessage(content=st.text_input("相談内容を入力してください")),
    ]

    if st.button("送信"):
        response = llm(message)
        st.write(response.content)

elif selected_item == "健康の専門家":
    st.write("健康の専門家に相談できます") 
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    message = [
    SystemMessage(content="あなたは健康の専門家です。"),
    HumanMessage(content=st.text_input("相談内容を入力してください")),
    ]

    if st.button("送信"):
        response = llm(message)
        st.write(response.content)
