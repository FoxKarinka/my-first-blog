# Django Girls Blog

This is a separate, English-language Django blog following the Django Girls
Tutorial's model, admin, URL, view, template, and static-file steps:
https://tutorial.djangogirls.org/en/

## Run on Windows

From this folder, create and activate a virtual environment, install Django,
create the database tables, and start the development server:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the blog or
http://127.0.0.1:8000/admin/ to manage posts.

If Windows cannot find `python`, use the full path to your Python executable
when creating the virtual environment.
