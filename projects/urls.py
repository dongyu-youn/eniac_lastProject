from django.urls import path
from .views import Project


urlpatterns = [
    path('project', Project, name="project"),
]