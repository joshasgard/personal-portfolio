from django.contrib import admin
from .models import Project

# Shows Project model in admin page
admin.site.register(Project)