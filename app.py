import os
import streamlit as st
import app.pages
import app.sidebar
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

# create a config dictionary
config = {
    "endpoint": os.environ["AZURE_OPENAI_ENDPOINT"],
    "api_key": os.environ["AZURE_OPENAI_KEY"],
    "api_version": os.environ["AZURE_OPENAI_API_VERSION"],
    "model": os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
}

# Initialize OpenAI client
client = AzureOpenAI(
    azure_endpoint=config["endpoint"],
    api_version=config["api_version"],
    api_key=config["api_key"],
)

# App home page
app.pages.show_home()

# app sidebar
with st.sidebar:
    appKey = app.sidebar.show_sidebar() or "4PHqt99DvHGK"

# Start LLM process
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question", key="submit", disabled=question == "")

if submit:
    if appKey == os.environ["APP_KEY"]:
        with st.spinner("Processing ..."):
            try:
                # Response generation
                full_response = ""
                message_placeholder = st.empty()

                messages = [
                    {
                        "role": "system",
                        "content": f"""
                            You are an expert in converting English questions to SQL query!
                            The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
                            SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
                            the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
                            \nExample 2 - Tell me all the students studying in Data Science class?, 
                            the SQL command will be something like this SELECT * FROM STUDENT 
                            where CLASS="Data Science"; 
                            also the sql code should not have ``` in beginning or end and sql word in output
                        """,
                    },
                    {"role": "user", "content": question},
                ]

                for completion in client.chat.completions.create(
                    model=config["model"],
                    messages=messages,
                    temperature=0,
                    max_tokens=1280,
                    stream=True,
                ):

                    if (
                        completion.choices
                        and completion.choices[0].delta.content is not None
                    ):
                        full_response += completion.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")

                message_placeholder.markdown(full_response)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Invalid Access Key!")
        st.stop()
