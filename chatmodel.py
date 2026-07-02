
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st


load_dotenv()


st.set_page_config(
    page_title="AI Chat Model",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 AI Chat Model")
st.write("Powered by LangChain + Gemini 2.5 Flash")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    GOOGLE_API_KEY = AQ.Ab8RN6Lv9fiGYDtYqbdEwYgz23Lml_NSCqsJ-bzI8kXkr5bkxg,
    temperature=0.7
)

# Store Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    
    response = llm.invoke(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.content)

    st.session_state.messages.append(
        {"role": "assistant", "content": response.content}
    )
