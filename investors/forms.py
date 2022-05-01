from django import forms
from .models import investor, investor_contact, investor_file

class InvestorForm(forms.ModelForm):

    class Meta:
        model = investor
        fields = ('name','short_name','reg_no','address','city','post_code','phone','key_contact','category','contact_email')
        labels ={
            'name':'Name',
            'short_name':'Short Name',
            'reg_no':'Registration Number',
            'address':'Business Address',
            'city':'City / State',
            'post_code':'Postal / Zip Code',
            'key_contact':'Key Contact Person',
            'contact_email':'Email Address',
            'phone':'Phone Number',
            'category':'Investor Category',
        }

    def __init__(self,*args,**kwargs):
        super(InvestorForm,self).__init__(*args,**kwargs)
        self.fields['category'].empty_label = "Select"

class ContactForm(forms.ModelForm):
    Model = investor_contact
    fields = ('name','phone','email','main_contact','adv_board_rep','inv_comm_rep','reports')
    labels ={
        'name':'Name',
        'phone':'Contact Phone Number',
        'email':'Email Address',
        'main_contact':'Key Contact',
        'adv_board_rep':'Advisory Board Representative',
        'inv_comm_rep':'Investement Committee Representative',
        'reports':'Receives Reports'
    }


class FileForm(forms.ModelForm):
    class Meta:
        model = investor_file
        fields = ('description','inv_file','investor')