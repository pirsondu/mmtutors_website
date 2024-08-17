from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index_page, name="home"),
    path("about", views.about_page, name="about"),
    path("features", views.features_page, name="features"),
    # path("contact", views.contact_page, name="contact"),
    path("blogs", views.blogs_page, name="blogs"),
    path("blog", views.blog_page, name="blog"),
    path("vlog", views.vlog_page, name="vlog"),
    path("privacy", views.privacy_page, name="privacy"),
    path("tutors/registration", views.tutor_register_page, name="tutor_registration"),
    path("tutors/events", views.tutor_events_page, name="tutor_events"),
    path("tutors/faq", views.tutor_faq_page, name="tutor_faq"),
    path("tutors/terms", views.tutor_terms_page, name="tutor_terms"),

    path("parents/faq", views.parent_faq_page, name="parents_faq"),
    path("parents/tutors", views.parent_tutors_page, name="parents_tutors"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
