import streamlit as st


# display the sidebar
def show_sidebar():
    st.subheader("💡Info", anchor=False)
    st.write(
        "This is a Streamlit app for **Text to SQL and RAG** handling both structured and unstructured data. It is powered by Azure OpenAI."
    )

    st.subheader("⚙️Settings", anchor=False)

    with st.container(border=True):
        appKey = st.text_input(
            "Access Key:",
            placeholder="8cb78***************",
            type="password",
        )

    st.subheader("🛠Technology Stack", anchor=False)
    st.write("Python, Streamlit, Azure OpenAI, Azure AI Search")
    st.write(
        "Check out the repo here: [Text to SQL and RAG](https://github.com/robrita/Azure-Text-SQL-RAG)"
    )

    return appKey
