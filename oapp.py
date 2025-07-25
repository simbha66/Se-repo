import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai

# ========== CONFIG ==========

GOOGLE_API_KEY = "AIzaSyD5D2CwnAb4bzsftkzHYIat_Fsj9ojyo_8"  # Replace with your Gemini API key
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ========== FUNCTIONS ==========

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def generate_appointment_letter(resume_text):
    prompt = f"""
You are an HR manager at Social Eagle.

Task: Generate a formal job appointment order based on the following resume content:

--- Resume Content Start ---
{resume_text}
--- Resume Content End ---

Instructions:
- Extract candidate's full name.
- Identify appropriate job title and skills.
- Write a professional appointment letter from Social Eagle.
- Include today's date and company name.
- Ensure it is suitable for sending via email.
- Use polite, clear, and HR-appropriate language.

Output only the formatted appointment letter.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# ========== STREAMLIT UI ==========

st.set_page_config(page_title="Social Eagle | Job Appointment Generator", layout="centered")

st.title("📄 Job Appointment Letter Generator")
st.subheader("Powered by Social Eagle HR • Gemini 2.0 Flash + Streamlit")

uploaded_file = st.file_uploader("Upload Resume (PDF Only)", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading and analyzing resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("Generate Appointment Letter"):
        with st.spinner("Generating letter using Gemini..."):
            letter = generate_appointment_letter(resume_text)
        st.success("✅ Appointment Letter Generated")
        st.markdown("---")
        st.markdown("### 📬 Appointment Letter")
        st.code(letter, language="markdown")
        st.download_button("📥 Download Letter as Text File", letter, file_name="appointment_letter.txt")
