# 🕵️ Job-Hunter-Agent  
**Your AI-Powered Junior Dev Job Scout**  

[![GitHub stars](https://img.shields.io/github/stars/aliii-codes/Job-Hunter-Agent?style=for-the-badge)](https://github.com/aliii-codes/Job-Hunter-Agent/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aliii-codes/Job-Hunter-Agent?style=for-the-badge)](https://github.com/aliii-codes/Job-Hunter-Agent/network)
[![GitHub issues](https://img.shields.io/github/issues/aliii-codes/Job-Hunter-Agent?style=for-the-badge)](https://github.com/aliii-codes/Job-Hunter-Agent/issues)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)  
![Python](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python)
![Cohere](https://img.shields.io/badge/cohere-AI-ff69b4?style=for-the-badge&logo=cohere)
![Gmail](https://img.shields.io/badge/gmail-SMTP-red?style=for-the-badge&logo=gmail)

---

## ✨ Highlights  

- **AI-Powered Filtering** 🚀: Uses Cohere's AI to match jobs to your unique profile  
- **Daily Email Updates** 📧: Get curated job matches delivered to your inbox  
- **Beginner-Friendly** 🌱: Focuses on junior, entry-level, and freelance roles  
- **Multi-Source Aggregation** 🌐: Fetches jobs from RemoteOK and Remotive  

---

## 📋 Features  

| Feature               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Job Fetching**      | Aggregates remote job listings from multiple sources (RemoteOK, Remotive)  |
| **Smart Filtering**   | Uses Cohere's AI to match jobs to your skills, experience, and preferences |
| **Hard Filtering**    | Automatically excludes senior-level roles                                  |
| **Daily Updates**     | Sends a daily email with curated job matches                               |
| **Customizable Profile** | Tailors job recommendations to your unique skills and experience          |

---

## 🛠️ Tech Stack  

| Category       | Technologies                                                                 |
|----------------|------------------------------------------------------------------------------|
| **Languages**  | Python                                                                      |
| **Libraries**  | `requests`, `cohere`, `schedule`, `smtplib`, `dotenv`                       |
| **APIs**       | Cohere API, RemoteOK API, Remotive API                                      |
| **Email**      | Gmail SMTP                                                                  |

---

## 🚀 Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/aliii-codes/Job-Hunter-Agent.git
   cd Job-Hunter-Agent
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**  
   Create a `.env` file with:  
   ```env
   COHERE_API_KEY=your_cohere_api_key
   EMAIL=your_email@gmail.com
   EMAIL_APP_PASSWORD=your_app_password
   ```

4. **Run the scheduler**  
   ```bash
   python scheduler.py
   ```

---

## 🛠 Usage  

| Action            | Command/Steps                                                                 |
|-------------------|-------------------------------------------------------------------------------|
| **Update Profile**| Modify `profile.py` with your details                                        |
| **Run Manually**  | Execute `python main.py` to fetch and filter jobs immediately                |
| **Automated Run** | The scheduler runs daily at 9 AM, sending email updates automatically        |

---

## 📂 Project Structure  

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

---

## 🤝 Contributing  

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

---

## 🐞 Bug Reports & Feature Requests  
Open an issue [here](https://github.com/aliii-codes/Job-Hunter-Agent/issues).  

---

## 📜 License & Acknowledgements  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  
Special thanks to Cohere, RemoteOK, and Remotive for their APIs.
