import streamlit as st
from modules import email_parser, summarizer

def main():
    st.set_page_config(page_title="LLM-Powered Email Assistant", layout="centered")
    st.title("📧 LLM-Powered Email Assistant")

    # File uploader
    uploaded_file = st.file_uploader("Upload a raw email (.txt)", type=["txt"], key="email_uploader")

    if uploaded_file:
        raw_email = uploaded_file.read().decode("utf-8")
        parsed = email_parser.parse_email(raw_email)

        st.subheader("📨 Email Details")
        st.markdown(f"**Subject:** {parsed['subject']}")
        st.markdown(f"**From:** {parsed['sender']}")
        st.text_area("Body", parsed['body'], height=200, key="email_body")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Summarize", key="summarize_btn"):
                summary = summarizer.summarize_email(parsed['body'])
                st.session_state['summary'] = summary
                st.subheader("📋 Summary")
                st.success(summary)

        with col2:
            if st.button("Generate Reply", key="reply_btn"):
                if 'summary' in st.session_state:
                    reply = summarizer.generate_reply(st.session_state['summary'])
                    st.subheader("✉️ Suggested Reply")
                    st.info(reply)
                else:
                    st.warning("Please summarize the email first.")

# Only run the app once
if __name__ == "__main__":
    main()
