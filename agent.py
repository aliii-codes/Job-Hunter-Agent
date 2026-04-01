import cohere
import json
import os
from profile import profile
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def filter_jobs(jobs):
    if not jobs:
        return []

    jobs_text = ""
    for i, job in enumerate(jobs):
        jobs_text += f"""
Job {i+1}:
Title: {job['title']}
Company: {job['company']}
Tags: {', '.join(job['tags']) if job['tags'] else 'none'}
URL: {job['url']}
Description: {job['description']}
---"""

    prompt = f"""
You are a job filter agent for a BEGINNER developer with this profile:

Name: {profile['name']}
Age: {profile['age']} years old (teenager, NOT a graduate)
Skills: {', '.join(profile['skills'])}
Looking for: {', '.join(profile['looking_for'])}
Preferred jobs: {', '.join(profile['preferred_jobs'])}
Experience: {profile['experience']} (self-taught, no degree, no professional experience)

Here are today's job listings:
{jobs_text}

Your task:
- STRICTLY EXCLUDE any job with these words in the title: Senior, Lead, Principal, Staff, Manager, Architect, Director
- ONLY include jobs tagged as: junior, entry-level, intern, beginner, freelance, or no experience required
- If unsure, EXCLUDE the job — it's better to return fewer jobs than wrong ones
- Rank them best match first
- Return ONLY a JSON array, no extra text, no markdown

Format:
[
  {{
    "title": "...",
    "company": "...",
    "url": "...",
    "reason": "why this is a good match in one sentence"
  }}
]
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt,
        temperature=0.3,
    )

    raw = response.text.strip()

    try:
        raw = raw.replace("```json", "").replace("```", "").strip()
        filtered = json.loads(raw)
        return filtered
    except Exception as e:
        print(f"Cohere parse error: {e}")
        print("Raw response:", raw)
        return []