# **Django Doc me :**

# django-docme :

---
Django Document me

package that let you create your docs not coding it  😉😉 .

---
#### we can split this package into 2 part , the frontend and the backend :

- **Frontend** build with sveltekit and skeleton UI .
- **backend** with djangorestframework and python .

## Before start

download the latest package from the releases [here](https://github.com/zarqizoubir/django-docme/releases)

or using curl  (to be fast and look cool 😎😎😎):
```bash
curl -o django-docme.tar.gz -L https://github.com/zarqizoubir/django-docme/releases/download/v0.2.0/django-docme-0.2.0.tar.gz
```

or if you want to use a specific version :

```bash
curl -o django-docme.tar.gz -L https://github.com/zarqizoubir/django-docme/releases/download/v0.2.0/django-docme-{version}.tar.gz
```

## Quick start
-----------

1. install the package from releases :
`pip install ./package_name.tar.gz`
2. add app to `setting.py` :
```python
INSTALLED_APPS = [
	...,
	"rest_framework",
	"docme",
	"mdeditor",
	...,
]


# File Uploading for Mdeditor 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

```

3. add this to `urls.py` :

```python
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	...,
	path(r'mdeditor/', include('mdeditor.urls')),
	path("docme/", include("docme.urls")), # Important don't change the docme/ urls otherwise it's not work .
	...,
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

4. Now you just need to add the view you like :

```python
from docme.views import index

urlpatterns = [
	...,
	path("your_path/", index), # enter the path you want 
]
```

5. migrate the db by running `python manage.py migrate` .
6. run the developent server `python manage.py runserver`.
7. visite the link `http://127.0.0.1:8000/your_path` .
and here you go .

<hr/>

This is just a quick setup and all the information could be found in website [here](https://zarqizoubir.github.io/django-docme)
