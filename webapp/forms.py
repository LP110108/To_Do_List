from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=256, required=True, label='Title')
    description = forms.CharField(max_length=2048, required=True, label='Text', widget=widgets.Textarea)
