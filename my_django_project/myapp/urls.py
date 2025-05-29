from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),       # This will be http://localhost:8000/my-app/
    path('about/', views.about_view, name='about'), # This will be http://localhost:8000/my-app/about/
]