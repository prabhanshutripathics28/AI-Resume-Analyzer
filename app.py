import streamlit as st
from utils import extract_text, preprocess, match_score, missing_skills, top_matching_words

st.markdown("# 🚀 AI Resume Analyzer")
st.caption("Analyze resumes using NLP • TF-IDF • Cosine Similarity")
st.write("Updated UI 🚀")

resume_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:
    resume_text = extract_text(resume_file)

    #  Show extracted content
    st.subheader("Extracted Resume Content")
    st.write(resume_text[:500])

    r = preprocess(resume_text)
    j = preprocess(job_desc)

    score = match_score(r, j)
    missing = missing_skills(r, j)
    top_words = top_matching_words(r, j)


    st.markdown("## 📊 Analysis Results")

    # Score Section
    st.markdown(f"### 🎯 Match Score: {score}%")
    st.progress(int(score))


    #  Feedback
    if score < 50:
        ...
        st.error(" Low match. Improve your resume.")
    elif score < 75:
        st.warning(" Decent match, but can improve.")
    else:
        st.success(" Strong match! You're good to go.")

    # Skills Section
    col1, col2 = st.columns(2)

    with col1:
    st.markdown("### ✅ Matching Skills")
    for skill in top_words:
        st.markdown(f"- {skill}")

    with col2:
    st.markdown("### ❌ Missing Skills")
    for skill in missing[:10]:
        st.markdown(f"- {skill}")

    report = f"""
Match Score: {score}%

Top Skills:
{', '.join(top_words)}

Missing Skills:
{', '.join(missing[:10])}
"""

st.download_button(
    label="📥 Download Report",
    data=report,
    file_name="resume_analysis.txt",
    mime="text/plain"
)