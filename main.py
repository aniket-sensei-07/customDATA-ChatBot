import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_csv_agent

def main():
    load_dotenv()

    st.set_page_config(page_title="Ask")
    st.header("Ask 📊")

    user_csv = st.file_uploader("Upload your data(CSV)", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your data.")

        llm = ChatGroq(
            temperature=0,
            model_name="llama-3.3-70b-versatile"
        )

        agent = create_csv_agent(
            llm,
            user_csv,
            verbose=True,
            allow_dangerous_code=True
        )

        if user_question:
            response = agent.run(user_question)
            st.write(response)

if __name__ == "__main__":
    main()

