import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
from pydantic.v1.fields import FieldInfo as FieldInfoV1

def main():
    load_dotenv()

    st.set_page_config(page_title="Ask")
    st.header("Ask")

    user_csv = st.file_uploader("Upload your data", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your data")

        llm = ChatOpenAI(
            temperature=0,
            model="gpt-4o-mini"
        )

        agent = create_csv_agent(
            llm,
            user_csv,
            verbose=True,
            allow_dangerous_code=True  # 👈 REQUIRED
        )

        if user_question:
            response = agent.run(user_question)
            st.write(response)

if __name__ == "__main__":
    main()