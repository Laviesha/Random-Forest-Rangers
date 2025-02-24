import nltk 

nltk.download("punkt")
nltk.download("stopwords")

from scraper import process_articles
from seo_optimizer import optimize_content
import time
import schedule
from scraper import process_articles
from publisher import publish_articles

def job():
    print("\n⏳ Running job: Fetching & Publishing news")
    process_articles()  # Scrape and save news
    publish_articles()  # Publish saved news

job()
# Schedule job every 30 minutes
schedule.every(30).minutes.do(job)

print("🚀 Application started! Fetching & publishing news every 30 minutes.")

start_time = time.time()
max_runtime =  60  # Run for 2 hours

while True:
    schedule.run_pending()
    print(f"🔄 Checking schedule... {time.strftime('%H:%M:%S')}")  
    time.sleep(10)  # Check every 10 seconds

    if time.time() - start_time > max_runtime:
        print("⏹️ Stopping application after 2 hours.")
        break