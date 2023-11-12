# Import data from excel to Django

## Install dependencies

macOS:

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
deactivate
source .venv/bin/activate
```

Windows:
```
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
deactivate
.venv\Scripts\activate
```

## Configure Django

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Launch Django admin

```
python manage.py runserver
```

Go to http://localhost:8000/admin

## Lauch Jupyter lab

```
jupyter lab
```

Open `import-from-excel.ipynb`