from django.contrib import admin
from django.urls import path,include
from services import views

urlpatterns = [
   
    path("location",views.location,name='location'),
    path("browse", views.browse_trips, name='browse'),
    path('search',views.search_view, name='search'),
    path("create",views.create_trip,name='create'),
     path("create_new/<int:pkid>",views.create_new,name='create_new'),
]
