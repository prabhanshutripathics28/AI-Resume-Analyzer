# 🚀 AI Resume Analyzer (NLP-based Matching System)

## 🌐 Live Demo
https://your-streamlit-link

An intelligent web application that analyzes resumes against job descriptions using Natural Language Processing (NLP).

## 🔥 Features
- Upload resume (PDF)
- Paste job description
- Calculates match score using TF-IDF + Cosine Similarity
- Identifies missing skills
- Interactive UI using Streamlit

## 🧠 Tech Stack
- Python
- Streamlit
- Scikit-learn
- SpaCy
- PyPDF2

## ⚙️ How it works
1. Extracts text from resume
2. Preprocesses text using NLP (lemmatization, stopword removal)
3. Converts text into vectors using TF-IDF
4. Computes similarity score
5. Displays missing skills

## ▶️ Run locally
```bash
pip install -r requirements.txt
python -m streamlit run app.py
