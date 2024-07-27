from django import forms
from .models import contact_view
from .models import register_view

class coderform(forms.ModelForm):
    class Meta:
        model = contact_view
        fields = ['name','email','message']
       

class coderregister(forms.ModelForm):
    class Meta:
        model = register_view
        fields = ['name','email', 'state','city','zipcode','suggestions']
       
