from django.urls import path
from . import views
URLPattern = [
    path('',views.home,name='home')

]