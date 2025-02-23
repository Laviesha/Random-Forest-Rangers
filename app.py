# import nltk

# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download("punkt_tab")

# from scraper import process_article

# from seo_optimizer import optimize_content

# # Example URL (replace with actual URL)
# article_url = "https://www.ndtv.com/delhi-news#pfrom=home-ndtv_mainnavigation"

# # Get article text and summary
# article_text, summary = process_article(article_url)

# if article_text and summary:
#     # Optimize the summary for SEO
#     seo_data = optimize_content(summary)

#     print("\n✅ SEO Optimization Results:")
#     print("SEO Title:", seo_data["title"])
#     print("Meta Description:", seo_data["description"])
#     print("Keywords:", seo_data["keywords"])
#     print("Optimized Summary:", seo_data["optimized_text"])
# else:
#     print("❌ Failed to extract text or summary.")

import nltk 

nltk.download("punkt")
nltk.download("stopwords")

from scraper import process_articles
from seo_optimizer import optimize_content

# Get all articles
articles = process_articles()

if not articles:
    print("❌ No articles found.")
    exit()

# Process each article
for idx, (article_text, summary) in enumerate(articles):
    print(f"\n📰 Article {idx+1}:")
    
    # Optimize the summary for SEO
    seo_data = optimize_content(summary)

    print("\n✅ SEO Optimization Results:")
    print("SEO Title:", seo_data["title"])
    print("Meta Description:", seo_data["description"])
    print("Keywords:", seo_data["keywords"])
    print("Optimized Summary:", seo_data["optimized_text"])
    print("\n" + "="*80)
