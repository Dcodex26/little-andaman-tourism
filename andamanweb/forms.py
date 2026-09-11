from django import forms

from .models import Enquiry


class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = [
            'name',
            'email',
            'phone',
            'subject',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address',
            }),

            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number',
            }),

            'subject': forms.TextInput(attrs={
                'placeholder': 'What would you like to know?',
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Write your enquiry here...',
                'rows': 6,
            }),
        }