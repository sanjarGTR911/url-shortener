from django.shortcuts import render
from django.http import HttpResponse # Import HttpResponse

def home_view(request):
    """
    A simple view to display a welcome message.
    """
    return HttpResponse("<h1>Welcome to My Django App!</h1><p>This is a custom page.</p>")

def about_view(request):
    """
    An 'About Us' page view.
    """
    return HttpResponse("<h2>About Us</h2><p>We are learning Django with Docker!</p>")