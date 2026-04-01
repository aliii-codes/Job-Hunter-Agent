from fetcher import fetch_all_jobs
from agent import filter_jobs
from mailer import send_email

EXCLUDED_KEYWORDS = ["senior", "lead", "principal", "staff", "manager", "architect", "director"]

def hard_filter(jobs):
    return [
        job for job in jobs
        if not any(word in job['title'].lower() for word in EXCLUDED_KEYWORDS)
    ]

def run():
    print("Job Hunter Agent starting...")
    
    jobs = fetch_all_jobs()
    
    if not jobs:
        print("No jobs fetched today.")
        return

    print("Cohere is filtering jobs for you...")
    filtered = filter_jobs(jobs)

    if not filtered:
        print("No matching jobs found today.")
        return

    
    filtered = hard_filter(filtered)

    if not filtered:
        print("All jobs were senior roles. Nothing to send today.")
        return

    print(f"Found {len(filtered)} matching jobs!")

    send_email(filtered)

if __name__ == "__main__":
    run()