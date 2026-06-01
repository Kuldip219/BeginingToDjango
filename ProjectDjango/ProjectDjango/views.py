from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World! This is the home page.")
    return render(request, 'index.html')  
def about(request):
    return HttpResponse("This is the about page. Here you can learn more about us.")

def contact(request):
    return HttpResponse("This is the contact page. Feel free to reach out to us!")