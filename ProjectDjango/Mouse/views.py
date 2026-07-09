from django.shortcuts import render
from .models import variety, Project
from django.shortcuts import get_object_or_404
from .forms import VarietyForm

# Create your views here.

def all_mouse(request):
    pages = variety.objects.all()
    return render(request, 'mouse/all_mouse.html', {'pages': pages})

def mouse_detail(request, mice_id):
    mice = get_object_or_404(variety, pk=mice_id)
    return render(request, 'mouse/mouse_detail.html', {'mice': mice})

def mouse_info(request):
    info = None
    if request.method == 'POST':
        form = VarietyForm(request.POST)
        if form.is_valid():
            selected_variety = form.cleaned_data['variety']
            projects = project.objects.filter(varieties=selected_variety)
    else:
        form = VarietyForm()        
    return render(request, 'mouse/mouse_info.html', {'info': info, 'form': form})