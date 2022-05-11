
## ¡quickstart

```python
> pip install django

> django-admin startproject mysite

> python manage.py runserver
```


## ¡new application
```python
### create new app
python manage.py startapp $app_name
```

## ¡DB, migrate
```python
### create admin user
> python manage.py createsuperuser

### create migration file
> python manage.py makemigrations $app_name

### show migration sql
> python manage.py sqlmigrate $app_name $migration_number

### exec migrate
> python manage.py migrate [$app_name] [$version]

### reset migrations
> python manage.py migrate $app_name zero

### show migrations
> python manage.py showmigrations [$app_name]


```

