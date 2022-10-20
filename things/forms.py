from django import forms
from .models import Thing

"""Forms of the project."""

# Create your forms here.


class ThingForm(forms.Form):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'name': forms.Textarea(), 'quantity': forms.NumberInput()}
