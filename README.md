# 🎓 InternHub

**InternHub** is a web application built to help students organize and manage their internship applications efficiently.  
It serves as a personal tracker — allowing users to add, view, and manage internship opportunities in one place.

---

## ✨ Features  

- 🔑 **User Authentication**  
  - Secure sign-up, log-in, and log-out functionality  
  - Passwords are hashed using Django’s built-in authentication system  
  - Session management handled through Django sessions  

- 📚 **Application Tracker**  
  - Add internship applications with details like company name, position, status, and deadline  
  - View, update, or delete applications directly from your dashboard  
  - See key statistics — total applications sent, interviews, and offers received
  - View websites for internships directly on the internship page
  - Light/dark mode feature using Alpine.js

---

## 🧰 Tech Stack  

- **Backend:** Django (Python)  
- **Database:** PostgreSQL  
- **Frontend:** Django Templating Language (DTL), Bootstrap 5, Alpine.js  
- **Authentication:** Django Auth System  

---

## 🚀 Overview  

InternHub provides students with a simple, intuitive dashboard to manage the entire internship process — from the first application to the final offer.  
It replaces messy spreadsheets and scattered notes with an organized digital solution powered by Django.

---

## 📊 Installation

```bash
git clone https://github.com/darkcom109/InternHub.git
cd internhub
pip install -r requirements.txt
python manage.py runserver
```
