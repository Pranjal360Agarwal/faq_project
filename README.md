# FAQ Management API

A Django-based FAQ API with multilingual support, caching, and an admin panel.

## Features
- Stores FAQs with WYSIWYG editor.
- Supports multi-language translations.
- Uses Redis caching for performance.
- REST API with query parameters.

## Setup
```bash
git clone <repo-url>
cd faq_project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Usage
```bash
# Fetch FAQs in English
curl http://localhost:8000/api/faqs/

# Fetch FAQs in Hindi
curl http://localhost:8000/api/faqs/?lang=hi
```
```bash


---

## **🐳 10. Add Docker Support**
### **Commit Message:**
```bash
git commit -m "feat: add Dockerfile and docker-compose for deployment"

---
```

## Code (Dockerfile):
```bash
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Code (docker-compose.yml):
```bash
version: "3.8"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - redis
  redis:
    image: "redis:alpine"
```

# Made with ❤ by [Pranjal Agarwal](https://github.com/Pranjal360Agarwal).