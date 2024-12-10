from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('success/', views.success, name='success'),
    path('error/', views.error, name='error'),
    path('download/', views.download_pdf, name='download_pdf'),
    path('detail/', views.detail_page, name='detail_page'),
]