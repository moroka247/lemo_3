from django import forms
from django.db import models
from django.forms import widgets
from .models import fund

class FundForm(forms.ModelForm):

    class Meta:
        model = fund
        fields = ('name','short_name','structure','objective','f_currency','target_commitment','investment_period','divestment_period')
        labels ={
            'name':'Name',
            'short_name':'Short Name',
            'structure_id':'Fund Structure',
            'objective':'Fund Objective',
            'f_currency':'Fund Currency',
            'target_commitment':'Target Commitment',
            'investment_period':'Investment Period',
            'divestment_period':'Divestment Period',
        }

        widgets = {
            'contents':forms.Textarea(attrs={
                'style':'height:100px;width:500px'
            }),
        }

    def __init__(self,*args,**kwargs):
        super(FundForm,self).__init__(*args,**kwargs)
        self.fields['structure'].empty_label = "Select"
        self.fields['f_currency'].empty_label = "Select"
        self.fields['short_name'].required = False,
        self.fields['target_commitment'].required = False,
        self.fields['investment_period'].required = False,
        self.fields['divestment_period'].required = False,
        


    

