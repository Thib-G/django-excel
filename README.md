# Import data from excel to Django

## Install dependencies

macOS:

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
deactivate
source .venv/bin/activate
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