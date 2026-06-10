from django.shortcuts import render

# Create your views here.

def all_mouse(request):
    return render(request, 'mouse/all_mouse.html')