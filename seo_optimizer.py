import re
import nltk
from textblob import TextBlob
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

# Download required NLP resources
nltk.download("punkt")
nltk.download("stopwords")
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))

def extract_keywords(text, top_n=5):
    """Extracts top keywords from text using TF-IDF."""
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in STOPWORDS]

    vectorizer = TfidfVectorizer(stop_words="english", max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform([" ".join(words)])

    keywords = vectorizer.get_feature_names_out()
    return ", ".join(keywords)

def generate_seo_title(summary):
    """Creates an engaging, keyword-rich SEO title."""
    blob = TextBlob(summary)
    noun_phrases = blob.noun_phrases

    # Pick an important noun phrase or create a title
    if noun_phrases:
        title = noun_phrases[0].title()
    else:
        title = "Breaking News: " + " ".join(summary.split()[:5]).title()

    return title[:60]  # Keep within Google's title length

def generate_meta_description(summary):
    """Creates an SEO-friendly meta description."""
    description = summary[:150].strip()
    if len(summary) > 150:
        description += "..."
    return description

def improve_readability(text):
    """Formats content for better readability (short sentences, easy words)."""
    sentences = nltk.sent_tokenize(text)
    improved_sentences = []

    for sentence in sentences:
        # Replace complex words using TextBlob's simplify method
        simplified = TextBlob(sentence).correct()
        improved_sentences.append(str(simplified))

    return " ".join(improved_sentences)

def optimize_content(summary):
    """Applies all SEO enhancements to a given summary."""
    optimized_summary = improve_readability(summary)
    keywords = extract_keywords(summary)
    title = generate_seo_title(summary)
    description = generate_meta_description(summary)

    seo_content = {
        "title": title,
        "description": description,
        "keywords": keywords,
        "optimized_text": optimized_summary
    }
    return seo_content