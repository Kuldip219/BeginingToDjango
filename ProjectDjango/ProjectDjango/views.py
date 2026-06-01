from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World! This is the home page.")

def about(request):
    return HttpResponse("This is the about page. Here you can learn more about us.")

def contact(request):
    return HttpResponse("This is the contact page. Feel free to reach out to us!")