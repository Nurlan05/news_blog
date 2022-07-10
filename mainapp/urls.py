from django.urls import path
from mainapp.views import *

app_name = "mainapp"

urlpatterns = [
    path('', index, name="index"),
    path('news-detail/<str:pk>/', newsDetail, name='news-detail'),
    path('news-create', newsCreate, name='news-create'),
    path('news-update/<str:pk>/', newsUpdate, name='news-update'),
    path('news-delete/<str:pk>/', newsDelete, name='news-delete'),
]
