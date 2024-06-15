from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about.html")

def features_page(request):
    return render(request, "features.html")

def events_page(request):
    return render(request, "events.html")

def contact_page(request):
    return render(request, "contact.html")