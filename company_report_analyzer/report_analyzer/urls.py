from django.urls import path
from . import views

urlpattern = [
    path('', views.upload_file, name='upload_file')
]