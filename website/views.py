from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about.html")

def features_page(request):
    return render(request, "features.html")


def contact_page(request):
    return render(request, "contact.html")

def blogs_page(request):
    return render(request, "blogs.html")

def blog_page(request):
    return render(request, "blog.html")

def vlog_page(request):
    return render(request, "vlog.html")


def tutor_register_page(request):
    return render(request, "tutors/registration.html")


def tutor_events_page(request):
    return render(request, "tutors/events.html")
    
def tutor_faq_page(request):
    return render(request, "tutors/faq.html")
    
def tutor_terms_page(request):
    return render(request, "tutors/terms.html")