from pymongo import MongoClient
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# MongoDB Connection
MONGO_URI = "mongodb+srv://soumyak:RandomForestRangers@newsscraperdb.bk444.mongodb.net/?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true"

print("🔄 Connecting to MongoDB...")
client = MongoClient(MONGO_URI)
db = client["NewsNexsus"]
articles_collection = db["News_articles"]
print("✅ Connected to MongoDB!")

# WordPress Credentials
WP_URL = "https://newsnexus9.wordpress.com/xmlrpc.php"
WP_USERNAME = "lavishak2003"
WP_PASSWORD = "newpass@?1"

print("🔄 Connecting to WordPress...")
try:
    wp = Client(WP_URL, WP_USERNAME, WP_PASSWORD)
    print("✅ Connected to WordPress!")
except Exception as e:
    print(f"❌ WordPress connection failed: {e}")

def publish_articles():
    """Fetch unpublished articles from MongoDB and publish them."""
    print("📰 Fetching unpublished articles from MongoDB...")

    articles = list(articles_collection.find({"published": False}))  # Convert to list to check length
    if not articles:
        print("🚨 No unpublished articles found!")
        return

    print(f"📌 Found {len(articles)} unpublished articles!")

    for article in articles:
        try:
            print(f"📝 Preparing article: {article['title']}")
            
            post = WordPressPost()
            post.title = article["title"]
            post.content = f"<h2>Summary: </h2><p>{article['summary']}</p><h3>Full Article</h3><p>{article['text']}</p><h5>Original Article Link: {article['link']} </h5>"
            post.post_status = "publish"

            print("🚀 Publishing to WordPress...")
            wp.call(NewPost(post))  # Publish to WordPress
            print(f"✅ Published: {article['title']}")

            # Update article status in MongoDB
            articles_collection.update_one({"_id": article["_id"]}, {"$set": {"published": True}})
            print("🔄 Updated MongoDB status: Published ✅")

        except Exception as e:
            print(f"❌ Error publishing article '{article['title']}': {e}")

if __name__ == "main":
    publish_articles()  # Allows manual execution if needed