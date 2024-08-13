from django.shortcuts import render
from .models import Parent_Question, Tutor_Question, HomeImage, Achievement

# Create your views here.


def index_page(request):
    slider = HomeImage.objects.all()
    context = {'features':
               {
                   'en': {
                       'header': 'Our Fetures',
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
                   'mm': {
                       'header': "Our Fetures",
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
               }, 'services':
               {
                   'en': {
                       'header': 'Our Services',
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
                   'mm': {
                       'header': "ဝန်ဆောင်မှုများ",
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
               },  'testimonials':
               {
                   'en': {
                       'header': 'Testimonials',
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
                   'mm': {
                       'header': "အသုံးပြုသူတို့ရဲ့ စကားသံ",
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
               'slider': slider
               }
    return render(request, "index.html", context)


def about_page(request):
    
    achievements = Achievement.objects.all()
    context = {
        'aboutUs': {
            'mm':
                'MMtutors ကို ၂၀၁၇ ခုနှစ် ဇူလိုင်လတွင် တည်ထောင်ခဲ့ပါသည်။ ထိုစဥ်မှစ၍ ယနေ့အချိန်အထိ မိဘများ၊ ကျောင်းသားများ၊ ဘာသာရပ်အမျိုးမျိုးကို သင်ယူလေ့လာသူများနှင့် စီးပွားရေးလုပ်ငန်းများအတွက် ပညာရေးဆိုင်ရာ ရည်မှန်းချက်များပြည့်မီစေရန် အကောင်းဆုံးအထောက်အကူပေးသော လုပ်ငန်းတခုအနေဖြင့် ရပ်တည်နေပါသည်။ ကျွန်ုပ်တို့အနေဖြင့် ကျောင်းစာဘာသာရပ်များနှင့် ဘာသာစကားအမျိုးမျိုး အပါအဝင် အခြားသော ဘာသာရပ်များအတွက်လည်း ထိရောက်မှုရှိသော သင်ကြားမှုများကို ဆောင်ရွက်ပေးလျက်ရှိပါသည်။',
            'en':
                'MMtutors was founded in July 2017. Since then, MMtutors has served as a tutoring platform that helps parents, students, learners, and businesses achieve their educational goals. We offer effective learning solutions for a variety of courses, including academic subjects, languages, and more.'


        },
        'achievements': achievements,
        'vision': {
            'mm': 'ကျောင်းစာဘာသာရပ်များ၊ အသက်မွေးဝမ်းကျောင်း ပညာရပ်များနှင့် ဘာသာစကားလေ့လာမှုတို့အတွက် စိတ်ချယုံကြည်ရဆုံး သင်ကြားမှုရင်းမြစ်တခုဖြစ်လာစေရန်မှာ ကျွန်ုပ်တို့၏ မျှော်မှန်းချက်ဖြစ်ပါသည်။',
            'en': 'Our vision is to be the most reliable learning source for all academic, professional development, and language pursuits.'
        },
        'mission': {
            'mm': 'အရည်အသွေးမြင့်မားပြီး ဆန်းသစ်တဲ့ ကျောင်းသားအခြေပြုသင်ကြားမှုများ၊ ဝန်ထမ်းများ၏ သင်ယူမှုတိုးတက်စေရန် အကြံဉာဏ်ပေးသော ဝန်ဆောင်မှုများ ပံ့ပိုးပေးခြင်းဖြင့် သင်ယူသူတို့၏ မျှော်မှန်းချက်များကို ကျော်လွန်လျက် သင်ယူမှုအရည်အသွေးများတိုးတက်လာစေရန်မှာ ကျွန်ုပ်တို့၏ ရည်ရွယ်ချက်ဖြစ်ပါသည်။',
            'en': "Our mission is to exceed our learners' expectations and enhance their learning outcomes and performance by consistently providing high-quality, innovative, and learner-centered training and HR consultancy services."
        }
    }
    return render(request, "about.html", context)


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
        'questions': QuestionSets
    }
    return render(request, "tutors/faq.html", context)


def tutor_terms_page(request):
    return render(request, "tutors/terms.html")


def parent_faq_page(request):
    QuestionSets = Parent_Question.objects.all()
    context = {
        'questions': QuestionSets
    }
    return render(request, "parents/faq.html", context)


def parent_tutors_page(request):
    return render(request, "parents/tutors.html")
