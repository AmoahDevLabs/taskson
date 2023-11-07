from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'address', 'age']


class DateForm(forms.Form):
    date = forms.DateField(
        label='Date of Birth',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
