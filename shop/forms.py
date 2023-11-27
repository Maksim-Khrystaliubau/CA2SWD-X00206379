# forms.py
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    comment = forms.CharField(widget=forms.Textarea, label='Your Comment')
