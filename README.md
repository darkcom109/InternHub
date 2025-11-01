# 🎓 InternHub

<p align="center">
  <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/-Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/-Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" />
  <img src="https://img.shields.io/badge/-Alpine.js-8BC0D0?style=for-the-badge&logo=alpinedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/-CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> 
</p>

**InternHub** is a web application built to help students organise and manage their internship applications efficiently.  
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

## Screenshots (Early Frontend Prototype)

<img width="959" height="448" alt="image" src="https://github.com/user-attachments/assets/1c89b3a7-849c-4e98-948d-5c1c4af0edac" />
<img width="959" height="445" alt="image" src="https://github.com/user-attachments/assets/57abb364-4b31-4073-adce-f91daeefe278" />
<img width="959" height="446" alt="image" src="https://github.com/user-attachments/assets/038f3852-ca98-4de8-b287-fd5f3a9263f4" />

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

Clone the Repository and Install Dependencies
```bash
# Clone the repository
git clone https://github.com/darkcom109/InternHub.git
cd internhub
# Install requirements
pip install -r requirements.txt
```

Setup Environment Variables
```bash
# Setup password for your postgresql database and settings.py secret key
DB_PASSWORD=
SECRET_KEY=
```

Run Django Server
```bash
# Run your Django server
python manage.py runserver
```
