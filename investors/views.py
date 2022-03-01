from gettext import install
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import investor, investor_contact
from .forms import ContactForm, InvestorForm

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from cms.ajax.views import (AjaxDetailView, AjaxCreateView, AjaxUpdateView, AjaxDeleteView)
#from cms.mixins import ModelMixin
#from cms.views import CoreListView


# Create your views here.

class InvestorList(ListView):
    model = investor
    template_name = 'investors/investors.html'
    context_object_name = 'investors'

def InvestorDetail(request, pk):
    inv = investor.objects.get(id=pk)
    contacts = investor_contact.objects.filter(contact_investor = inv)
    context = {
        'investor': inv,
        'contacts': contacts
    }
    return render(request,'investors/investor_overview.html',context)




def inv_contact(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ContactForm()
        else:
            contact = investor_contact.objects.get(pk=id)
            form = ContactForm(instance=contact)
        return render(request,"investors/investor_overview.html",{'inv_contact':form})
    else:
        if id == 0:
            form = ContactForm(request.POST)
        else:
            contact = investor_contact.objects.get(pk=id)
            form = InvestorForm(request.POST, instance=contact)
        
        if form.is_valid():
            instance = form.save(commit=False)
            print("valid")
            instance.save()
        
            #return redirect(request,"investors/investor_overview.html")

    context = {}
    return render(request,'',context)


def add_investor(request):
    if request.method == 'POST':
        form = InvestorForm(request.POST)
    else:
        form = InvestorForm()

    return render(request,'investors.html/',{"form":form})


def investor_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = InvestorForm()
        else:
            selected_investor = investor.objects.get(pk=id)
            form = InvestorForm(instance=selected_investor)
        return render(request,"investors/investor_form.html",{'investor':form})
    else:
        if id==0:
            form = InvestorForm(request.POST)
        else:
            selected_investor = investor.objects.get(pk=id)
            form = InvestorForm(request.POST, instance=selected_investor)
        if form.is_valid():
            instance = form.save(commit=False)
            print("Valid")
            instance.save()
            return redirect('/investors/')
