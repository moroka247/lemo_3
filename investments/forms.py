from django import forms
from django.db import models
from .models import company, investment

class CompanyForm(forms.ModelForm):

    class Meta:
        model = company
        fields = ('co_name','co_short_name','co_reg_no','co_description','co_industry','co_country')
        labels ={
            'co_name': 'Company Name',
            'co_short_name': 'Company Short Name',
            'co_reg_no':'Company Registration Number',
            'co_description':'Company Description',
            'co_industry':'Industry',
            'co_country':'Country of Residence'
        }

    def __init__(self,*args,**kwargs):
        super(CompanyForm,self).__init__(*args,**kwargs)
        self.fields['co_industry','co_country'].empty_label = "Select"

class InvestmentForm(forms.ModelForm):

    class Meta:
        model = investment
        fields = ('inv_company','inv_fund','inv_instrument','inv_commitment','inv_disbursed','perf_status','inv_stage')
        labels ={
            'inv_company': 'Company Name',
            'inv_fund': 'Fund',
            'inv_instrument':'Investment Instrument',
            'inv_commitment':'Amount Committed',
            'inv_disbursed':'Amount Disbursed',
            'perf_status':'Performance Status',
            'inv_stage':'Stage of Transaction'
        }

    def __init__(self,*args,**kwargs):
        super(InvestmentForm,self).__init__(*args,**kwargs)
        self.fields['inv_company','inv_fund','inv_instrument','perf_status','inv_stage'].empty_label = "Select"