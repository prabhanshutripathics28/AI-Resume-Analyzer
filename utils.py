from PyPDF2 import PdfReader
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)


vectorizer = TfidfVectorizer()


def match_score(resume, job_desc):
    vectors = vectorizer.fit_transform([resume, job_desc])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)


def missing_skills(resume, job_desc):
    resume_words = set(resume.split())
    job_words = set(job_desc.split())
    return list(job_words - resume_words)


# 🔥 NEW FEATURE
def top_matching_words(resume, job_desc):
    resume_words = set(resume.split())
    job_words = set(job_desc.split())

    common = resume_words.intersection(job_words)
    return list(common)[:10]