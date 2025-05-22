from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "MMtutors Admin"
admin.site.site_title = "MMtutors Admin Portal"
admin.site.index_title = "Welcome to MMtutors Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("website.urls"))
]
