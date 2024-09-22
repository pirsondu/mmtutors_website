from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
        
        # labels = {
        #     "Event": ""
        #     "guest_name" : "Your Name",
        #     "guest_email" : "Your Email",
        #     "guest_phone" : "Your Phone",
        # }
