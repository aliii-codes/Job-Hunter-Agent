import requests

REMOTEOK_URL = "https://remoteok.com/api"
REMOTIVE_URL = "https://remotive.com/api/remote-jobs"

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_remoteok():
    try:
        res = requests.get(REMOTEOK_URL, headers=HEADERS)
        jobs = res.json()[1:] 
        return [
            {
                "title": j.get("position", ""),
                "company": j.get("company", ""),
                "tags": j.get("tags", []),
                "url": j.get("url", ""),
                "description": j.get("description", "")[:300],
            }
            for j in jobs
        ]
    except Exception as e:
        print(f"RemoteOK error: {e}")
        return []

def fetch_remotive():
    try:
        res = requests.get(REMOTIVE_URL, params={"category": "software-dev"})
        jobs = res.json().get("jobs", [])
        return [
            {
                "title": j.get("title", ""),
                "company": j.get("company_name", ""),
                "tags": j.get("tags", []),
                "url": j.get("url", ""),
                "description": j.get("description", "")[:300],
            }
            for j in jobs
        ]
    except Exception as e:
        print(f"Remotive error: {e}")
        return []

def fetch_all_jobs():
    print("Fetching jobs...")
    jobs = fetch_remoteok() + fetch_remotive()
    print(f"Found {len(jobs)} jobs total")
    return jobs