from django.urls import path
from . import views

urlpatterns = [
    path('/o', views.home, name='home'),
    path('/about', views.about, name='about'),
]