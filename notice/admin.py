from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Article)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['title']