from django.contrib import admin

# Register your models here.
from user.models import register
admin.site.register(register)