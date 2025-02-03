from rango.models import Category

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

In your project directory (e.g. <workspace>/<project_name>/), create a new directory called static and a new directory called images inside static.

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

# 5. Models

All models have an auto-increment integer field called id which is automatically assigned and acts a primary key.

- `CharField`: a field for storing character data (e.g. strings). Specify max_length to provide a maximum number of characters that a CharField field can store.
```python
models.CharField(max_length=128)
```

- `URLField`: much like a CharField, but designed for storing resource URLs. You may also specify a max_length parameter.
```python
models.URLField()
```

- `IntegerField`: which stores integers.
```python
models.IntegerField(default=0)
```

- `DateField`: which stores a Python `datetime.date` object.

Django provides three types of fields for forging relationships between models in your database.
  - `ForeignKey`, a field type that allows us to create a one-to-many relationship12;
  - `OneToOneField`, a field type that allows us to define a strict one-to-one relationship13;
  - `ManyToManyField`, a field type which allows us to define a many-to-many relationship

**Tips:**

- **Always Implement __str__() in your Classes**
`__str__()` is the Python equivalent of the `toString()` method!

- **Don’t git push your Database!**
Add db.sqlite3 to your .gitignore file so that it won’t be added when you git commit and git push.


Django provides what is called a **migration tool** to help us set up and update the database to reflect any changes to your models.
1.First of all, the database must be initialised. This means that creating the database and all the associated tables so that data can then be stored within it/them.
```bash
python manage.py migrate
```

2. Next, create a superuser to manage the database.
```bash
python manage.py createsuperuser
```

3. Whenever you **make changes** to your app’s models, you need to register the changes via the `makemigrations` command in `manage.py`.
```bash
python manage.py makemigrations rango
```

> If you want to check out the underlying SQL that the Django ORM issues to the database engine for a given migration
> `python manage.py sqlmigrate rango 0001`

4. After you have created migrations for your app, you need to commit them to the database
```bash
python manage.py migrate
```

5. Interact with Django models
```bash
python manage.py shell

# Import the Category model from the Rango application 
>>> from rango.models import Category

# Create a new category object, and save it to the database.
>>> c = Category(name='Test') 
>>> c.save()
```

6. Registers both the `Category` and `Page` class to the admin interface
```python
# rango/admin.py
from django.contrib import admin 
from rango.models import Category, Page 

admin.site.register(Category) 
admin.site.register(Page)
```

# 6. Creating a Model instance (population Script)
**An automated script will mean each collaborator can simply run that script to initialise the database on their computer with the same sample data as you.**

make sure you have imported your project’s settings by importing django and setting the environment variable DJANGO_SETTINGS_MODULE to be your project’s setting file. Then call `django.setup()` to import your Django project’s settings
```python
# Create this file in <workspace>/tango_with_django_project/
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
# ......
```

```python
"""
populate_rango.py
get_or_create() return the tuple that is(instance, created) = Model.objects.get_or_create(...)
instance is model object, created will show true or false
[0] can get instance that is Category object
"""

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
```

**Summary**

**Adding a model**
1. create new model(s)
2. Update admin.py and register new model(s) if you want to make them accessible to the `admin interface`.
3. run `python manage.py makemigrations <app_name>`
4. run `python manage.py migrate`
5. Create/edit population script

**Sometimes you have to delete database**
1. delete `db.sqlite3`
2. migrate
3. run `python manage.py createsuperuser`
4. run population script

**customize the admin form**
```python
# <app_name>/admin.py
class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category',               {'fields': ['category']}),
        ('Details', {'fields': ['title', 'url', 'views']}),
    ]

admin.site.register(Page, PageAdmin)
admin.site.register(Category)
```
this will help to divide attributes into two columns

**Adding related objects**
Django knows that a ForeignKey should be represented in the admin as a <select> box. But, really, this is an inefficient way of adding related objects to the system.

```python
class PageInline(admin.StackedInline):
    model = Page
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category Info',               {'fields': ['name']}),
        ('Community', {'fields': ['views', 'likes'], 'classes': ['collapse']}),# collapse，默认折叠
    ]
    #  让 Page 作为 Category 的 Inline
    inlines = [PageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
```
```python
# 实现字段纵向排列
class ChoiceInline(admin.TabularInline):
    # ...
```

**Customize the admin change list**
让admin主页显示其余属性的内容
```python
class CategoryAdmin(admin.ModelAdmin):
    # ...
    list_display = ('views', 'likes')

```
**为admin添加过滤器**
```python
class Category(models.Model):
    # ...
    def was_most_views(self):
      return self.objects.order_by('-views').first()
  
# CategoryAdmin
list_filter = ['views']
```


