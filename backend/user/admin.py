from django.contrib import admin
from django.db import models
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'recommended', 'status', 'feedback')

admin.site.register(User, UserAdmin)