from django import forms
from django.db import models
from .models import investment

class InvestmentForm(forms.ModelForm):

    class Meta:
        model = investment
        fields = '__all__'
        labels ={

        }
