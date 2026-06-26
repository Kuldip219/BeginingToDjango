from django.shortcuts import render
from .models import variety

# Create your views here.

def all_mouse(request):
    pages = variety.objects.all()
    return render(request, 'mouse/all_mouse.html', {'pages': pages})