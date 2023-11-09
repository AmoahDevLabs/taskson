from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    date = forms.DateField(
        label='Date of Birth',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = Person
        fields = ['name', 'address', 'age', 'date']
