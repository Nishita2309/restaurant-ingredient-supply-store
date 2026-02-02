## Restaurant Ingredient Supply Store

A Django web application for browsing and managing restaurant ingredient supplies, including deals, bestsellers, premium products, a shopping cart, and order history.

---

## Tech Stack

- **Backend**: Django 4.2
- **Language**: Python 3
- **Database (dev)**: SQLite (`db.sqlite3`)
- **Static / Media**: Django staticfiles, local media storage

---

## Project Structure (high level)

- `manage.py` – Django CLI entrypoint
- `restaurant_ingredient_supply_store/` – project settings and URL configuration
- `store/` – main app (models, views, templates, URLs)
- `store/templates/store/` – HTML templates
- `store/static/` & `staticfiles/` – CSS, JS, and images
- `products_images/` – product images used by the app
- `requirements.txt` – Python dependencies

---

## Prerequisites

- **Python 3.x** installed and on your PATH
- **PowerShell** (Windows 10/11)

You do **not** need Docker or PostgreSQL for local development; SQLite is used by default.

---

## Setup & Run (Windows / PowerShell)

From a new PowerShell window:

### 1. Go to the project directory

```powershell
cd "C:\Users\nishi\OneDrive\Desktop\restaurant_ingredient_supply_store"
```

### 2. Create a virtual environment (once)

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
venv\Scripts\Activate.ps1
```

If you get an execution policy error:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Apply migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 6. (Optional) Create an admin user

```powershell
python manage.py createsuperuser
```

### 7. Run the development server

```powershell
python manage.py runserver
```

Then open in your browser:

- **Site**: `http://127.0.0.1:8000/`
- **Admin**: `http://127.0.0.1:8000/admin/`

Keep the PowerShell window running while you use the site.

---

## Common Issues & Fixes

- **"No module named 'django'"**
  - Make sure the virtual environment is active:  
    `venv\Scripts\Activate.ps1`
  - Then install dependencies:  
    `python -m pip install -r requirements.txt`

- **Browser says "127.0.0.1 refused to connect"**
  - The server isn’t running or crashed. Start it:  
    `python manage.py runserver`
  - Check the PowerShell window for error messages.

- **Port already in use**
  - Run on another port, for example:
    ```powershell
    python manage.py runserver 8001
    ```
  - Then open `http://127.0.0.1:8001/`.

---

## Deployment Notes

- `requirements.txt`, `Procfile`, and `render.yaml` are included for deployment to platforms like Render or similar PaaS providers.
- For production, you should:
  - Set `DEBUG = False`
  - Configure `ALLOWED_HOSTS`
  - Use a production database (e.g., PostgreSQL) and proper static/media hosting.

