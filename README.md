# Autonomous News Summarizer AI Agent

![WhatsApp Image 2025-02-24 at 21 39 45_98c35896](https://github.com/user-attachments/assets/b529e285-c6fb-47af-907b-47b2a5346ef4)

![WhatsApp Image 2025-02-24 at 21 42 30_b6ebd4f7](https://github.com/user-attachments/assets/f0640307-8fbb-436d-abeb-5b9417ec35dd)

## Overview  
This project automates news scraping, summarization, SEO optimization, and publishing to a WordPress site. It consists of multiple modules for handling different functionalities, from web scraping to content optimization and automated publishing.  

## Features  
- Scrapes news articles from NDTV (Delhi News).  
- Extracts and summarizes articles using an NLP model.  
- Enhances content with SEO optimization.  
- Stores processed articles in MongoDB.  
- Publishes articles to a WordPress blog automatically.  
- Runs on a scheduled interval.  

## Modules  

### 1. `app.py` (Main Application)  
- Schedules and runs the entire process every 30 minutes.  
- Calls `process_articles()` for scraping and summarizing.  
- Calls `publish_articles()` to publish content to WordPress.  

**Dependencies:**  
`schedule`, `nltk`, `scraper.py`, `publisher.py`, `seo_optimizer.py`  

### 2. `scraper.py` (News Scraper)  
- Fetches NDTV Delhi news articles.  
- Extracts links and processes articles using `newspaper3k`.  
- Summarizes content using `summarizer.py`.  
- Optimizes content for SEO with `seo_optimizer.py`.  
- Stores articles in MongoDB if not previously stored.  

**Dependencies:**  
`requests`, `BeautifulSoup`, `newspaper3k`, `pymongo`, `summarizer.py`, `seo_optimizer.py`  

### 3. `publisher.py` (WordPress Publisher)  
- Fetches unpublished articles from MongoDB.  
- Publishes content to WordPress using `wordpress_xmlrpc`.  
- Updates MongoDB to mark articles as published.  

**Dependencies:**  
`pymongo`, `wordpress_xmlrpc`  

### 4. `scheduler.py` (Task Scheduler)  
- Runs `publish_articles()` at set intervals.  
- Stops execution after a predefined runtime.  

**Dependencies:**  
`schedule`, `time`, `publisher.py`  

### 5. `seo_optimizer.py` (SEO Enhancer)  
- Extracts keywords using TF-IDF.  
- Generates SEO-friendly titles and meta descriptions.  
- Improves readability by simplifying text.  

**Dependencies:**  
`nltk`, `TextBlob`, `sklearn.feature_extraction.text.TfidfVectorizer`  

### 6. `summarizer.py` (Text Summarization)  
- Uses a pre-trained BART model (`facebook/bart-large-cnn`).  
- Produces concise and informative summaries.  

**Dependencies:**  
`transformers`, `torch`  

## Installation  

### Step 1: Install Dependencies  
```bash
pip install requests beautifulsoup4 pymongo newspaper3k wordpress-xmlrpc nltk transformers torch schedule
```

### Step 2: Download NLTK Resources  
```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
```

### Step 3: Configure Credentials  
- Update MongoDB and WordPress credentials in `publisher.py`.  

## Usage  

### Run the Main Application  
```bash
python app.py
```

### Run Scraper Separately  
```bash
python scraper.py
```

### Run Publisher Separately  
```bash
python publisher.py
```

## Notes  
- Ensure MongoDB is running and accessible.  
- Update WordPress credentials before running.  
- Modify `scheduler.py` for different scheduling intervals.  

## Team Members  
- [Lavisha Kapoor](https://github.com/Laviesha)  
- [Kanishka Soni](https://github.com/Kanishka-IITR)  
- [Soumya Kumari](https://github.com/VictoryVortex6)  

## Website  
🔗 [Live Blog](https://newsnexus9.wordpress.com)  
