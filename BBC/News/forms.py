from django import forms
from .models import News

class NewstForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['headline', 'content', 'reporter', 'image', 'date_reported']