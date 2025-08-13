# BlogBook Django

A modern, full-featured blogging platform built with **Django**, **Tailwind CSS**, and **cloud-hosted** for speed, robustness, and scalability.

---

## ✨ Features

- ✍️ **Create, edit, and delete blog posts** with images
- 📚 Organized blog structure (main app: `blogbook`, project: `mainblog`)
- ⚡ Responsive, beautiful UI powered by Tailwind CSS
- 🌐 Hosted free on Render, with **S3 cloud storage** for persistent uploads
- 🔒 Secure configuration with environment variables for secrets and database
- 🏞️ Media files stored on **Amazon S3** for limitless, persistent access

---

## 🚀 Quick Start

### 1. Clone the Repository

git clone https://github.com/pythoneer-sp/BlogBook-Django

### 2. Create & Activate Virtual Environment

python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt


### 4. Set Environment Variables

Create a `.env` file or set them in your hosting dashboard (Render, etc.):

DJANGO_SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url
RENDER_EXTERNAL_HOSTNAME=your-render-hostname

### 5. Apply Migrations

python manage.py makemigrations
python manage.py migrate

### 6. Collect Static Files

python manage.py collectstatic --noinput

### 7. Create Superuser

python manage.py createsuperuser

### 8. Run Locally

python manage.py runserver


## 🤝 Contributing

Pull requests are welcome! For significant changes, please open an issue first to discuss what you'd like to change.

---


**Special Thanks:**  
Render, Tailwind CSS, Django, and all the open-source communities ❤️
