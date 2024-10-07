from django.shortcuts import render
from . import models
# Create your views here.

def Project(request):
    projects = models.Project.objects.all()
    context = {
        "message": "hello", 
        "project": projects  # 문자열 "home"을 키로 설정
    } 
    return render(request, "project/project.html", context) 