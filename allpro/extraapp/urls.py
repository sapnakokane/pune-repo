from django.contrib import admin
from django.urls import path
from extraapp import views

urlpatterns = [
    path('morn/',views.morn),
    ]