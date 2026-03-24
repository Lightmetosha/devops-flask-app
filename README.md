DevOps Flask App 🚀

Production-like DevOps project demonstrating end-to-end deployment of a Python web application using Docker, Jenkins, GitHub Actions, Nginx, and HTTPS.

```markdown
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-pipeline-red)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-black)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange)
![HTTPS](https://img.shields.io/badge/HTTPS-Let's_Encrypt-brightgreen)

## Live Demo

https://lightmeserv.ru

## Overview

This project demonstrates a complete DevOps workflow:

- developing a Flask web application
- containerizing the application with Docker
- configuring CI/CD with GitHub Actions
- configuring CI/CD with Jenkins Pipeline as Code
- deploying the application to an Ubuntu VPS
- exposing the service through Nginx reverse proxy
- enabling HTTPS with Let's Encrypt

## 📸 Screenshots

### 🌐 Application
<img src="images/app.png" width="600"/>

## Architecture

```text
User
  ↓
Nginx (reverse proxy + HTTPS)
  ↓
Docker container (Flask app)
  ↑
CI/CD (GitHub Actions / Jenkins)
  ↑
GitHub repository

.
├── .github/workflows/
│   ├── ci.yml
│   └── cd.yml
├── templates/
│   └── index.html
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── .gitignore
└── README.md
