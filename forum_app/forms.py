from django import forms
from authentication_app.models import Profile
from .models import *

#для форума
class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст'}),
        }


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['text', 'image', 'seriousness']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опишите проблему'}),
            'seriousness': forms.Select(attrs={'class': 'form-control'}),
        }