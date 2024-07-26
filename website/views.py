from django.shortcuts import render
from .models import Parent_Question, Tutor_Question, HomeImage

# Create your views here.
def index_page(request):
    slider = HomeImage.objects.all()
    context = { 'features' : 
        {
            'en' : {
                'header' : 'Our Fetures',
                'topic1': {
                    'header': 'Qualified Tutors',
                    'body': '(Learn from the best tutors in the country)'
                },
                'topic2': {
                    'header': 'Flexible Scheduling',
                    'body': '(Adjust the timetable for the lessons)'
                },
                'topic3': {
                    'header': 'Interactive teaching',
                    'body': '(Engage with interactive and fun lessons)'
                }
            },
            'mm' : {
                'header' : "Our Fetures",
                'topic1': {
                    'header': 'အရည်အချင်းပြည့်ဝသော ဆရာများ',
                    'body': '(ပြည်တွင်းက အကောင်းဆုံးဆရာများနှင့် သင်ယူလိုက်ပါ)'
                },
                'topic2': {
                    'header': 'အချိန်စာရင်း ညှိနှိုင်းနိုင်ခြင်း',
                    'body': '(ကျောင်းသားနဲ့ဆရာနဲ့ အချိန်ကို ညှိပြီး သင်ယူနိုင်ခြင်း)'
                },
                'topic3': {
                    'header': 'အပြန်အလှန် သင်ကြားပေးခြင်း',
                    'body': '(သင်ခန်းစာများကို ပေါ့ပေါ့ပါးပါး ပျော်ပျော်ရွှင်ရွှင်နဲ့နားလည်လာအောင် သင်ကြားပေးခြင်း)'
                }
            }
        }, 'services' : 
        {
            'en' : {
                'header' : 'Our Services',
                'topic1': {
                    'header': 'Government Curriculum Subject Tutors',
                },
                'topic2': {
                    'header': 'International Curriculum Subject Tutors',
                },
                'topic3': {
                    'header': 'Languages & Others',
                }
            },
            'mm' : {
                'header' : "ဝန်ဆောင်မှုများ",
                'topic1': {
                    'header': 'အစိုးရသင်ရိုးညွှန်းတမ်းသင် ဆရာများ',
                },
                'topic2': {
                    'header': 'နိုင်ငံတကာ သင်ရိုးညွှန်းတမ်းသင် ဆရာများ',
                },
                'topic3': {
                    'header': 'ဘာသာစကားနှင့် အခြားပညာရပ် ဆရာများ',
                }
            }
        },  'testimonials' : 
        {
            'en' : {
                'header' : 'Testimonials',
                'topic1': {
                    'header': 'Government Curriculum Subject Tutors',
                },
                'topic2': {
                    'header': 'International Curriculum Subject Tutors',
                },
                'topic3': {
                    'header': 'Languages & Others',
                }
            },
            'mm' : {
                'header' : "အသုံးပြုသူတို့ရဲ့ စကားသံ",
                'topic1': {
                    'header': 'အစိုးရသင်ရိုးညွှန်းတမ်းသင် ဆရာများ',
                },
                'topic2': {
                    'header': 'နိုင်ငံတကာ သင်ရိုးညွှန်းတမ်းသင် ဆရာများ',
                },
                'topic3': {
                    'header': 'ဘာသာစကားနှင့် အခြားပညာရပ် ဆရာများ',
                }
            }
        }, 
        'slider' : slider
    }
    return render(request, "index.html", context)

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
    QuestionSets = Tutor_Question.objects.all()
    context = {
        'questions' : QuestionSets
    }
    return render(request, "tutors/faq.html", context)
    
def tutor_terms_page(request):
    return render(request, "tutors/terms.html")


    
def parent_faq_page(request):
    QuestionSets = Parent_Question.objects.all()
    context = {
        'questions' : QuestionSets
    }
    return render(request, "parents/faq.html", context)

    
def parent_tutors_page(request):
    return render(request, "parents/tutors.html")