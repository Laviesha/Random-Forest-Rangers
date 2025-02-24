import time
import schedule
from publisher import publish_articles

# Schedule to run every 30 minutes
schedule.every(1).minutes.do(publish_articles)  # Run every 1 min for testing

print("⏳ Scheduler started... Running publish_articles() every 1 minute.")

start_time = time.time()  # Store start time
max_runtime = 30  # Run for 5 minutes (for testing)

while True:
    schedule.run_pending()
    print(f"🔄 Checking schedule... {time.strftime('%H:%M:%S')}")  # Debugging message
    time.sleep(10)  # Check every 10 seconds

    # Stop after max_runtime
    if time.time() - start_time > max_runtime:
        print("⏹️ Scheduler stopped after max_runtime.")
        break