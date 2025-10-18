from django.urls import path

from . import views

urlpatterns = [
    path("welcome/<name>", views.welcome, name="welcome"),
]