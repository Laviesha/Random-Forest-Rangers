# import re
# import spacy
# from collections import Counter
# from summarizer import summarize_text

# # Load NLP model for keyword extraction
# nlp = spacy.load("en_core_web_sm")

# def clean_text(text):
#     """Removes special characters, extra spaces, and unnecessary formatting."""
#     text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
#     text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
#     return text

# def extract_keywords(text, num_keywords=5):
#     """Extracts important keywords from the text."""
#     doc = nlp(text)
#     words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
#     keywords = [word[0] for word in Counter(words).most_common(num_keywords)]
#     return ', '.join(keywords)

# def generate_seo_title(title):
#     """Enhances the title for SEO using keyword optimization."""
#     title = clean_text(title)
#     if len(title) > 60:  
#         title = title[:57] + "..."  # Ensure it's within the SEO limit
#     return f"{title} | Latest News & Updates"

# def generate_meta_description(summary):
#     """Generates an SEO-friendly meta description."""
#     summary = clean_text(summary)
#     if len(summary) > 160:
#         summary = summary[:157] + "..."  # Truncate to fit meta tag limits
#     return summary

# def optimize_article(article):
#     """Optimizes article data for SEO."""
#     optimized_article = {
#         "title": generate_seo_title(article["title"]),
#         "summary": summarize_text(article["summary"]),
#         "keywords": extract_keywords(article["summary"]),
#         "meta_description": generate_meta_description(article["summary"])
#     }
#     return optimized_article

# # Example usage
# if __name__ == "__main__":
#     example_article = {
#         "title": "Delhi Pollution Crisis Worsens as AQI Reaches Hazardous Levels",
#         "summary": "Delhi is facing severe pollution issues as the AQI has reached hazardous levels. Government officials are planning to impose restrictions on vehicle movement..."
#     }
    
#     optimized = optimize_article(example_article)
#     print("🔹 SEO Optimized Title:", optimized["title"])
#     print("🔹 Keywords:", optimized["keywords"])
#     print("🔹 Meta Description:", optimized["meta_description"])

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