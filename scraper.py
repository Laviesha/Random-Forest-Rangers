import requests
from bs4 import BeautifulSoup
import newspaper
from urllib.parse import urljoin
from summarizer import summarize_text  
from pymongo import MongoClient
import ssl
from seo_optimizer import optimize_content

# Base URL of the website
BASE_URL = "https://www.ndtv.com"
url = 'https://www.ndtv.com/delhi-news#pfrom=home-ndtv_mainnavigation'
headers = {"User-Agent": "Mozilla/5.0"}

print("🚀 Script started.")
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("❌ Failed to fetch page.")
    exit()

soup = BeautifulSoup(response.text, 'lxml')
print("✅ Page fetched successfully.")

# MongoDB Connection
MONGO_URI = "mongodb+srv://soumyak:RandomForestRangers@newsscraperdb.bk444.mongodb.net/?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true"

try:
    client = MongoClient(MONGO_URI)
    db = client["NewsNexsus"]
    articles_collection = db["News_articles"]
    print("🛢 Connected to MongoDB successfully.")
except Exception as e:
    print(f"❌ MongoDB Connection Error: {e}")

# Function to extract and summarize article
def process_article(url):
    try:
        print(f"📄 Processing article: {url}")
        article = newspaper.Article(url=url, language='en')
        article.download()
        article.parse()

        if not article.text:
            print("⚠ No text found in article.")
            return None, None
        
        summary = summarize_text(article.text)  # Call summarizer
        headline = article.title
        return headline, article.text, summary

    except Exception as e:
        # print(f"❌ Error processing {url}: {e}")
        return None, None, None

# Function to check if an article already exists in MongoDB
def is_article_stored(title):
    existing_article = articles_collection.find_one({"title": title})
    if existing_article:
        return True  # Article already exists
    return False  # Article does not exist

# Function to process multiple articles
def process_articles():
    article_links = []
    
    for link in soup.find_all('a', href=True):
        if link.find('img'):
            continue
        text = link.get_text(strip=True)
        full_url = urljoin(BASE_URL, link['href'])
        if len(text) > 20 and full_url.startswith(BASE_URL):
            article_links.append(full_url)

    print(f"🔍 Found {len(article_links)} articles.")

    for idx, article_url in enumerate(article_links[:2]):  # Limiting to 10 for testing
        headline, text, summary = process_article(article_url)
        if summary is None:
            # print(f"⚠ Skipping article {article_url} due to missing summary.")
            continue
        seo_data = optimize_content(text)

        if text and summary:
            # Check if article already exists in MongoDB
            if is_article_stored(headline):
                continue  # Skip storing if article already exists

            # Insert new article into MongoDB
            article_data = {
                "title": headline,
                "text": text,
                "summary": summary,
                "link": article_url,
                "published": False  # Default unpublished
            }
            try:
                articles_collection.insert_one(article_data)
                print(f"✅  {seo_data['title']} stored in MongoDB!")
            except Exception as e:
                print(f"❌ Error storing article {seo_data['title']} : {e}")

    print("📌 All articles stored in MongoDB.")

# Run the script
if __name__ == "main":
    process_articles()