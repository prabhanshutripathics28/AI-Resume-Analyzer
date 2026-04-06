import streamlit as st
from utils import extract_text, preprocess, match_score, missing_skills, top_matching_words

st.title("🚀 AI Resume Analyzer (NLP-based Matching System)")

resume_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:
    resume_text = extract_text(resume_file)

    # 🔥 Show extracted content
    st.subheader("Extracted Resume Content")
    st.write(resume_text[:500])

    r = preprocess(resume_text)
    j = preprocess(job_desc)

    score = match_score(r, j)
    missing = missing_skills(r, j)
    top_words = top_matching_words(r, j)

    # 🔥 Results
    st.subheader(f"Match Score: {score}%")

    st.subheader("Top Matching Skills")
    st.write(top_words)

    st.subheader("Missing Skills")
    st.write(missing[:10])

    # 🔥 Feedback
    if score < 50:
        st.error("❌ Low match. Improve your resume.")
    elif score < 75:
        st.warning("⚠️ Decent match, but can improve.")
    else:
        st.success("✅ Strong match! You're good to go.")