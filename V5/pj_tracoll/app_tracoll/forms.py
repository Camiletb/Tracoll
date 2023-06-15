import datetime
from django import forms
from django.core.exceptions import ValidationError
# class TranslationForm(forms.Form):
#     name = forms.CharField(label="Your name")
#     surname = forms.CharField(label="Your surname")
#     # translated_title = forms.CharField(max_length=100, required=False, help_text="Translate the original title to italian")
#     # def clean_translated_title(self):
#     #     data = self.cleaned_data['translated_title']
#     #     return data
    
#     #     if data < datetime.date.today():
#     #         raise ValidationError('Invalid - renewal in past')
#     #     if data > (datetime.date.today() +
#     #         datetime.timedelta(weeks=4)):
#     #         raise ValidationError('Invalid date - too late')

from django import forms
from .models import Translation

class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ['title', 'content']