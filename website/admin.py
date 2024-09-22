from django.contrib import admin
from .models import Parent_Question, Tutor_Question, HomeImage, Achievement, Testimonial, Category, Post, Event, Registration
class PostAdmin (admin.ModelAdmin):
    list_filter = ("categories",)
    list_display = ("title", "date", "excerpt")
    prepopulated_fields = {"slug": ("title",)}

class RegistrationAdmin (admin.ModelAdmin):
    list_filter = ("event",)
    list_display = ("guest_name", "guest_email", "guest_phone", "event")

admin.site.register(Parent_Question)
admin.site.register(Tutor_Question)
admin.site.register(HomeImage)
admin.site.register(Achievement)
admin.site.register(Testimonial)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Event)
admin.site.register(Registration, RegistrationAdmin)


