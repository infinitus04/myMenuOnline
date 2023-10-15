from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:linkId>', views.serve, name='serve'),
    path('', views.homePage)
]
