# 1 Creating Project

1. Creating Project

```bash
django-admin.py startproject <project_name>

# Creating app
python manage.py startapp <app_name>
```

2. modify the settings.py file: add rango

```python
INSTALLED_APPS = [ 
  'django.contrib.admin', 
  'django.contrib.auth', 
  'django.contrib.contenttypes', 
  'django.contrib.sessions', 
  'django.contrib.messages', 
  'django.contrib.staticfiles', 
  'rango',
]
```

3. creating View


4. Mapping URLs

- <project_name>/urls.py 
    - `path('<app_name>/', include('app_name.urls'))`
    - e.g., `path('rango/', include('rango.urls'))`

- <app_name>/urls.py
  ```python
    # e.g.,
    app_name = 'rango' 
    urlpatterns = [ path('', views.index, name='index'), ]
  ```


