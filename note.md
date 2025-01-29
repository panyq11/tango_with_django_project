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
  
# 2. Templates

Open project’s `settings.py` file, modifying `DIRS` list
```python
'DIRS': ['<workspace>/tango_with_django_project/templates']
```
But, it will become **problem** due to different path on different computers.

`BASE_DIR`: This variable stores the path to the directory in which project’s settings.py module is contained
```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```

We can then use our new TEMPLATE_DIR variable to replace the hard-coded path we defined earlier in TEMPLATES.
```python
# Make sure put this underneath the definition of BASE_DIR
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

'DIRS': [TEMPLATE_DIR,]
```

`Render`: This function takes as input the user’s request, the template filename, and the context dictionary

# 3. Static Media Files

In your project directory (e.g. <workspace>/<project_name>/), create a new directory called static and a new directory called images inside static.![img.png](static/images/rango.jpg)

- create a variable called STATIC_DIR at the top of settings.py
```python
STATIC_DIR = os.path.join(BASE_DIR, 'static')
```

- then create a new data structure called STATICFILES_DIRS
```python
STATICFILES_DIRS = [STATIC_DIR, ]
```

-Finally, check that the STATIC_URL variable
```python
STATIC_URL = '/static/'
```

- using images with HTML source
```html
<!-- index.html -->

<!DOCTYPE html>
{% load staticfiles %}

<img src="{% static 'images/rango.jpg' %}" alt="Picture of Rango" />
```

# 4. Serving Media Files

In your project directory (e.g. <workspace>/<project_name>/), create a new directory called media.

- edit settings.py
```python
# settings.py
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

MEDIA_ROOT = MEDIA_DIR

MEDIA_URL = '/media/
```

- Within the context_processors list, add a new string to include an additional context processor: `'django.template.context_processors.media'`
```python
'context_processors': [ 
  'django.template.context_processors.debug', 
  'django.template.context_processors.request', 
  'django.contrib.auth.context_processors.auth', 
  'django.contrib.messages.context_processors.messages', 
  'django.template.context_processors.media', # Check/add this line!
],
```

- <project name>/urls.py
```python
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [ ...
# ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```html
<img src="{{ MEDIA_URL }}cat.jpg" alt="Picture of Cat" />
```
