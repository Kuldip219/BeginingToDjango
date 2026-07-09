from django.shortcuts import render
from .models import variety
from django.shortcuts import get_object_or_404

# Create your views here.

def all_mouse(request):
    pages = variety.objects.all()
    return render(request, 'mouse/all_mouse.html', {'pages': pages})

def mouse_detail(request, mice_id):
    mice = get_object_or_404(variety, pk=mice_id)
    return render(request, 'mouse/mouse_detail.html', {'mice': mice})

def mouse_info(request):
    return render(request, 'mouse/mouse_info.html')