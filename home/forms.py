from django import forms

class CreateCarForm(forms.Form):
    name = forms.CharField(label="اسم السيارة", max_length=100)