from django.conf.urls import url
from homepage import views



urlpatterns=[
    url(r'^$', views.index, name='home'),
    # url(r'^About$', views.about, name='about'),

]
