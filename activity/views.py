from django.shortcuts import render
from . import models

# Create your views here.

def activity(request):
    activity = models.Activity.objects.all()
    context = {
        "activity": activity
    }
   
    return render(request, "activity.html", context)