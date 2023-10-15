from django.contrib import admin
from services.models import trips
from services.models import locs

# Register your models here.
admin.site.register(trips)
admin.site.register(locs)