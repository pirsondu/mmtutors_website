from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "MMTutors Admin"
admin.site.site_title = "MMTutors Admin Portal"
admin.site.index_title = "Welcome to MMTutors Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("website.urls"))
]
