# Kinetiq Support & Services Module Backend

## To set up locally:

### Clone the repo

```
$ git clone https://github.com/Kinetiq-PLM/kinetiq-erp-sales-backend
```

### In CMD or PS terminal, create venv (virtual environment) // preferably python ver 3.12 

```
python -m venv venv
```

### Activate venv

```
venv\scripts\activate
```

### Install requirements

```
pip install -r requirements.txt
```

### Uncomment and modify this to your own DB for local DB settings (go to support_and_services_backend/support_and_services_backend.settings.py):

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rds-local', # test db, not the db team's db
        'USER': 'postgres',
        'PASSWORD': 'lansservices',
        'HOST': 'localhost',
        'PORT': '5432',
        #'OPTIONS': {'options': '-c search_path=sales,services,human_resources,public'}
    }
}
```

### Uncomment to use RDS Kinetiq DB:

```
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'Kinetiq-DB'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'KntBg3jIY0DbpH8G9bwt'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '15432'),
    }
}
```

## Make sure server is running (local or RDS) before doing these steps:

```
// in terminal while venv is activated

cd support_and_services_backend
python manage.py runserver

// can optionally modify port to run different multiple server at once (8000 is the default port)
python manage.py runserver 8001
```

## URLs listed in urls.py can now be used to connect to frontend