# your_app_name/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('patent_list/', views.patent_list, name='patent_list'),
    path('',views.base,name='base'),
    path('search/',views.search,name='search')# Add other URLs as needed
]
