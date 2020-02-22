"""event_analytics URL Configuration

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    # Adds Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),

    # redirect other URLs to logs_app/urls.py for processing
    path('', include('logs_app.urls')),
]
