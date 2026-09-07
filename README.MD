## 🎨  Flask GUI – CI/CD Demo Application

This project is a lightweight **Python Flask web application** containerized with **Docker** to demonstrate **CI/CD and DevOps fundamentals**.

The application serves a colorful, interactive web interface and dynamically displays runtime system information such as:
- Hostname
- IP Address
- FQDN
- Current Date

This information is retrieved from inside the container, making the app useful for understanding how applications behave across different environments.

---

## 🎯 Purpose of This Project

This project was created to:
- Demonstrate Docker image build and container execution
- Serve as a practical CI/CD demo using **GitHub Actions** and **Jenkins**
- Validate environment-specific metadata inside containers
- Act as a simple deployable app for Kubernetes, EC2, and cloud platforms

---

## 🚀 How to Run the Application

### Option 1: Run using Docker (Recommended)

```bash
docker build -t flask-ci-cd-app .
docker run -d -p 80:80 flask-ci-cd-app

