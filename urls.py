from django.urls import re_path as url
from homepage import views



urlpatterns=[
    url(r'^$', views.index, name='home'),
]