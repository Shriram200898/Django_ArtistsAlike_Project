from django.core import validators
from django import forms
from .models import Category
from .models import Feedback
from .models import Order

class AddOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Category_Name','Category_Description']
        widgets = {
            'Category_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Category_Description': forms.Textarea(attrs={'class': 'form-control','rows':5}),
        }


