# Job-Hunter-Agent

## Project Title & Description
**Job-Hunter-Agent** is an automated job search tool designed for beginner developers. It fetches remote job listings, filters them based on a user's profile, and sends daily email updates with relevant job matches. Ideal for self-taught developers looking for entry-level or freelance opportunities.

## Features
- **Job Fetching**: Aggregates job listings from multiple sources (RemoteOK, Remotive).
- **Smart Filtering**: Uses Cohere's AI to filter jobs based on user profile and preferences.
- **Daily Updates**: Sends a daily email with curated job matches.
- **Customizable Profile**: Tailors job recommendations to individual skills and experience.
- **Hard Filtering**: Excludes senior-level roles to focus on beginner-friendly jobs.

## Tech Stack
- **Languages**: Python
- **Libraries**: `requests`, `cohere`, `schedule`, `smtplib`, `dotenv`
- **APIs**: Cohere API, RemoteOK API, Remotive API
- **Email**: Gmail SMTP

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/aliii-codes/Job-Hunter-Agent.git
   cd Job-Hunter-Agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in a `.env` file:
   ```env
   COHERE_API_KEY=your_cohere_api_key
   EMAIL=your_email@gmail.com
   EMAIL_APP_PASSWORD=your_app_password
   ```
4. Run the scheduler:
   ```bash
   python scheduler.py
   ```

## Usage
1. **Update Profile**: Modify `profile.py` with your details.
2. **Run Manually**: Execute `python main.py` to fetch and filter jobs immediately.
3. **Automated Run**: The scheduler runs daily at 9 AM, sending email updates automatically.

## Project Structure
```
Job-Hunter-Agent/
├── agent.py          # Job filtering logic using Cohere API
├── fetcher.py        # Job fetching from external APIs
├── mailer.py         # Email sending functionality
├── main.py           # Main execution script
├── profile.py        # User profile configuration
├── scheduler.py      # Daily job scheduler
├── .env              # Environment variables (not included in repo)
└── requirements.txt  # Project dependencies
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
