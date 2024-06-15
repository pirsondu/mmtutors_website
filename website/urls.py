from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index_page, name="home"),
    path("about", views.about_page, name="about"),
    path("features", views.features_page, name="features"),
    path("events", views.events_page, name="events"),
    path("contact", views.contact_page, name="contact"),
    path("blogs", views.blogs_page, name="blogs"),
    path("blog", views.blog_page, name="blog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
