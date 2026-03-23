# 🚀 DevOps Flask App

A small production-like DevOps project that demonstrates application deployment to a Linux VPS using Docker, GitHub Actions, and SSH-based CI/CD.

---

## 📌 Project Overview

This project demonstrates a basic end-to-end DevOps workflow:

- Deploying a Python Flask application on an Ubuntu VPS
- Containerizing the application with Docker
- Managing source code with Git and GitHub
- Configuring CI/CD with GitHub Actions
- Performing automatic deployment to a remote server over SSH
- Using healthcheck endpoints and container restart policies

---

## 🏗️ Architecture

```text
Developer
   ↓
GitHub Repository
   ↓
GitHub Actions (CI/CD)
   ↓
Ubuntu VPS
   ↓
Docker Container
   ↓
Flask Application
