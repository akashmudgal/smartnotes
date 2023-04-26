from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('',include('home.urls')),
    path('smart/',include('notes.urls')),
    path('admin/', admin.site.urls)
]
