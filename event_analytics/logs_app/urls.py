from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('visualize', views.visualize, name='visualize'),
    path('logged_out', views.logged_out, name='logout'),
]