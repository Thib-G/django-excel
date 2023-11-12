from django.contrib import admin
from .models import Function, Person, Project

# Register your models here.
admin.site.register(Function)
admin.site.register(Person)
admin.site.register(Project)
