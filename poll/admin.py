from django.contrib import admin
from django.db import models
from django.contrib import admin
from .models import Choice, Question

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)