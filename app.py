import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]


# Configure Gemini
genai.configure(api_key=api_key)

@st.cache_resource
def get_model():
    return genai.GenerativeModel("models/gemini-1.5-flash")

model = get_model()
st.set_page_config(page_title="GenAI Multi-Tool", layout="wide")
st.title("🤖 Gemini-Powered Multi-Tool Assistant")

tabs = st.tabs(["💬 Chatbot", "📄 Summarizer", "🧠 Code Explainer", "📋 Resume Helper", "💡 Idea Generator"])
with tabs[0]:
    st.subheader("💬 Freeform Chatbot")
    prompt = st.chat_input("Ask me anything...")

    if prompt:
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
            st.markdown("**Response:**")
            st.write(response.text)
with tabs[1]:
    st.subheader("📄 Summarizer")
    text = st.text_area("Paste text to summarize:")

    if st.button("Summarize"):
        prompt = f"Summarize the following text:\n{text}"
        with st.spinner("Summarizing..."):
            response = model.generate_content(prompt)
            st.markdown("**Summary:**")
            st.write(response.text)
with tabs[2]:
    st.subheader("🧠 Code Explainer")
    code = st.text_area("Paste your code (Python, C, etc.):")

    if st.button("Explain Code"):
        prompt = f"Explain this code in simple terms:\n{code}"
        with st.spinner("Analyzing code..."):
            response = model.generate_content(prompt)
            st.code(code, language="python")
            st.markdown("**Explanation:**")
            st.write(response.text)
with tabs[3]:
    st.subheader("📋 Resume Reviewer")
    resume_text = st.text_area("Paste your resume text:")

    if st.button("Get Feedback"):
        prompt = f"Review and suggest improvements for this resume:\n{resume_text}"
        with st.spinner("Reviewing..."):
            response = model.generate_content(prompt)
            st.markdown("**Suggestions:**")
            st.write(response.text)
with tabs[4]:
    st.subheader("💡 Idea Generator")
    topic = st.text_input("Enter a topic (e.g., AI, Education, Health):")

    if st.button("Generate Ideas"):
        prompt = f"Suggest 3 innovative project ideas related to {topic}."
        with st.spinner("Generating ideas..."):
            response = model.generate_content(prompt)
            st.markdown("**Ideas:**")
            st.write(response.text)
