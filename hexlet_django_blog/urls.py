from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog.views import index, about


urlpatterns = [
    path('', index),
    path('article/', include('hexlet_django_blog.article.urls')),
    path('admin/', admin.site.urls),
    path('about/', about, name="about")
]
