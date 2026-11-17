from django import forms
from .models import Contact

class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact

        fields = [
            'name',
            'email',
            'phone',
            'service',
            'message'
        ]
    def clean_name(self):
        name=self.cleaned_data['name'].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "Please enter a valid name"
            )
        return name
    def clean_message(self):
        message =self.cleaned_data['message'].strip()

        if len(message) < 10:
            raise forms.ValidationError(
                "Message must contain at least 10 characterss ." 
            )
        return message