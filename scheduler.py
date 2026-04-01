import schedule
import time
from main import run

# runs every day at 9am
schedule.every().day.at("09:00").do(run)

print("Scheduler running... Job Hunter will email you daily at 9am")

while True:
    schedule.run_pending()
    time.sleep(60)
