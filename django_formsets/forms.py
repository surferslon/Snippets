
from django import forms
from django.conf import settings
from django.forms.models import formset_factory

class DataRemoveForm(forms.Form):
    selected = forms.BooleanField(required=False)
    app = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
                          attrs={'style': 'readonly': True}))
    model = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
                            attrs={'style': 'readonly': True}))

RemovableObjectsFormset = formset_factory(DataRemoveForm)