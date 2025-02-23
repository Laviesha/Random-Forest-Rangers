# import requests
# from bs4 import BeautifulSoup

# # Step 1: Fetch HTML
# url = 'https://www.ndtv.com/delhi-news#pfrom=home-ndtv_mainnavigation'
# html_text = requests.get(url).text
# soup = BeautifulSoup(html_text, 'lxml')

# # Step 2: Extract all <a> tags that are NOT inside an <img> tag
# for link in soup.find_all('a', href=True):
#     # Step 3: Ignore <a> tags that are inside an <img> tag
#     if link.find('img'):  
#         continue  # Skip if <a> tag contains an <img>

#     text = link.get_text(strip=True)  # Get the text inside <a>
#     if len(text) > 20:  # Ignore short links (to filter out unwanted text)
#         print(f"📰 Title: {text}")
#         print(f"🔗 Link: {link['href']}\n")


# import requests
# from bs4 import BeautifulSoup
# import newspaper
# import json
# from urllib.parse import urljoin  # To handle relative URLs

# # Base URL of the website
# BASE_URL = "https://www.ndtv.com"

# # Step 1: Fetch HTML
# url = 'https://www.ndtv.com/delhi-news#pfrom=home-ndtv_mainnavigation'
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print("Failed to fetch page.")
#     exit()

# soup = BeautifulSoup(response.text, 'lxml')

# # Step 2: Function to extract article text
# def extract_article_text(url):
#     try:
#         article = newspaper.Article(url=url, language='en')
#         article.download()
#         article.parse()

#         article_data = {
#             "title": str(article.title),
#             "text": str(article.text),
#             "authors": article.authors,
#             "published_date": str(article.publish_date),
#             "top_image": str(article.top_image),
#             "videos": article.movies,
#             "keywords": article.keywords,
#             "summary": str(article.summary)
#         }

#         print(f"📰 Title: {article_data['title']}")
#         print(f"📅 Published Date: {article_data['published_date']}")
#         print(f"📜 Text: {article_data['text'][:500]}...")  # Print first 500 characters
#         print("-" * 80)

#         return article_data

#     except Exception as e:
#         print(f"Error extracting article from {url}: {e}")
#         return None

# # Step 3: Extract all <a> tags that are NOT inside an <img> tag
# article_links = []

# for link in soup.find_all('a', href=True):
#     if link.find('img'):  
#         continue  # Skip <a> tags that contain <img>

#     text = link.get_text(strip=True)  # Get the text inside <a>
#     full_url = urljoin(BASE_URL, link['href'])  # Convert to absolute URL

#     if len(text) > 20 and full_url.startswith(BASE_URL):  # Filter short titles and external links
#         print(f"📰 Title: {text}")
#         print(f"🔗 Link: {full_url}\n")
#         article_links.append(full_url)

# # Step 4: Extract and print details for each article
# print(f"Found {len(article_links)} article links.\n")

# for idx, article_url in enumerate(article_links[:5]):  # Limit to 5 articles for testing
#     print(f"Scraping Article {idx + 1}/{len(article_links)}:")
#     extract_article_text(article_url)


# import requests
# from bs4 import BeautifulSoup
# import newspaper
# import json
# from urllib.parse import urljoin
# from summarizer import summarize_text  # Import summarization function
# # from pymongo import MongoClient

# # # MongoDB Connection
# # MONGO_URI = "mongodb+srv://soumyak:RandomForestRangers@newsscraperdb.bk444.mongodb.net/?retryWrites=true&w=majority&appName=NewsScraperDB"
# # client = MongoClient(MONGO_URI)
# # db = client["news_db"]
# # articles_collection = db["articles"]

# # Base URL of the website
# BASE_URL = "https://www.ndtv.com"
# url = 'https://www.ndtv.com/delhi-news#pfrom=home-ndtv_mainnavigation'
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print("❌ Failed to fetch page.")
#     exit()

# soup = BeautifulSoup(response.text, 'lxml')

# # Function to extract and summarize article
# def process_article(url):
#     try:
#         article = newspaper.Article(url=url, language='en')
#         article.download()
#         article.parse()

#         if not article.text:
#             # print(f"⚠ Skipping empty article: {url}")
#             return
#         # print(article.text)
#         # print("---------------------------------------------------")
#         summary = summarize_text(article.text)  # Call summarizer

#         article_data = {
#             "url": url,
#             "title": article.title,
#             "summary": summary,
#             "authors": article.authors,
#             "published_date": article.publish_date,
#             "top_image": article.top_image
#         }
        
#         #print("printing summary:\n",summary)
#         return article.text, summary
#         # # Store summarized article in MongoDB
#         # articles_collection.insert_one(article_data)
#         # print(f"✅ Summarized & Stored: {article.title}")

#     except Exception as e:
#         # print(f"❌ Error processing {url}: {e}")
#           print(" ")
# # Extract article links
# article_links = []
# for link in soup.find_all('a', href=True):
#     if link.find('img'):
#         continue
#     text = link.get_text(strip=True)
#     full_url = urljoin(BASE_URL, link['href'])
#     if len(text) > 20 and full_url.startswith(BASE_URL):
#         article_links.append(full_url)

# # Process each article
# print(f"🔍 Found {len(article_links)} articles.")
# for idx, article_url in enumerate(article_links[:5]):  # Limit to 5 for testing
#     process_article(article_url)

# # print("✅ All articles summarized & stored in MongoDB.")



# import requests
# from bs4 import BeautifulSoup
# import newspaper
# from urllib.parse import urljoin
# from summarizer import summarize_text  
# from pymongo import MongoClient


# # Base URL of the website
# BASE_URL = "https://www.ndtv.com"
# url = 'https://www.ndtv.com/delhi-news#pfrom=home-ndtv_mainnavigation'
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print("❌ Failed to fetch page.")
#     exit()

# soup = BeautifulSoup(response.text, 'lxml')



# # MongoDB Connection
# MONGO_URI = "mongodb+srv://soumyak:RandomForestRangers@newsscraperdb.bk444.mongodb.net/?retryWrites=true&w=majority&appName=NewsScraperDB"
# client = MongoClient(MONGO_URI)
# db = client["news_db"]
# articles_collection = db["articles"]


# # Function to extract and summarize article
# def process_article(url):
#     try:
#         article = newspaper.Article(url=url, language='en')
#         article.download()
#         article.parse()

#         if not article.text:
#             return None, None
        
#         summary = summarize_text(article.text)  # Call summarizer
#         return article.text, summary

#     except Exception as e:
#         print(f"❌ Error processing {url}: {e}")
#         return None, None

# # ✅ **Define process_articles() function properly**
# def process_articles():
#     """Extracts multiple articles from NDTV and returns summaries."""
#     article_links = []
    
#     for link in soup.find_all('a', href=True):
#         if link.find('img'):
#             continue
#         text = link.get_text(strip=True)
#         full_url = urljoin(BASE_URL, link['href'])
#         if len(text) > 20 and full_url.startswith(BASE_URL):
#             article_links.append(full_url)

#     print(f"🔍 Found {len(article_links)} articles.")

#     for idx, article_url in enumerate(article_links[:5]):  # Limiting to 5 for testing
#         text, summary = process_article(article_url)
#         if text and summary:
#             # 🆕 Save article in MongoDB
#             article_data = {
#                 "title": f"Article {idx+1}",
#                 "text": text,
#                 "summary": summary,
#                 "published": False  # Default unpublished
#             }
#             articles_collection.insert_one(article_data)
#             print(f"✅ Article {idx+1} stored in MongoDB!")

#     print("📌 All articles stored in MongoDB.")
    
#     articles = []
#     for idx, article_url in enumerate(article_links[:5]):  # Limiting to 5 for testing
#         text, summary = process_article(article_url)
#         if text and summary:
#             articles.append((text, summary))
    
#     return articles


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
    db = client["news_db"]
    articles_collection = db["articles"]
    print("🛢️ Connected to MongoDB successfully.")
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
            print("⚠️ No text found in article.")
            return None, None
        
        summary = summarize_text(article.text)  # Call summarizer
        return article.text, summary

    except Exception as e:
        print(f"❌ Error processing {url}: {e}")
        return None, None

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

    for idx, article_url in enumerate(article_links[:10]):  # Limiting to 5 for testing
        text, summary = process_article(article_url)
        seo_data = optimize_content(summary)
        if text and summary:
            article_data = {
                "title": seo_data["title"],
                "text": text,
                "summary": summary,
                "published": False  # Default unpublished
            }
            try:
                articles_collection.insert_one(article_data)
                print(f"✅  {seo_data['title']} stored in MongoDB!")
            except Exception as e:
                print(f"❌ Error storing article {seo_data['title']} : {e}")

    print("📌 All articles stored in MongoDB.")

# Run the script
if __name__ == "__main__":
    process_articles()
