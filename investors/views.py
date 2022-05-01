from contextvars import Context
from gettext import install
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import investor, investor_contact, investor_file
from .forms import ContactForm, InvestorForm, FileForm
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class InvestorList(ListView):
    model = investor
    template_name = 'investors/investors.html'
    context_object_name = 'investors'

def InvestorDetail(request, pk):
    inv = investor.objects.get(id=pk)
    contacts = investor_contact.objects.filter(contact_investor = inv)
    files = investor_file.objects.filter(investor = inv)
    context = {
        'investor': inv,
        'contacts': contacts,
        'files':files
    }
    return render(request,'investors/investor_overview.html',context)


def add_investor(request):
    form = InvestorForm()
    if request.method == 'POST':
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/investors/')
        messages.info(request,"INVESTOR ADDED SUCCESSFULLY!")
    
    context = {
        'investor':form,
    }
    return render(request,"investors/investor_form.html",context)

    
def update_investor(request,inv_id):
    selected_investor = investor.objects.get(id=inv_id)
    form = InvestorForm(instance = selected_investor)

    if request.method =="POST":
        form = InvestorForm(request.POST, instance=selected_investor)

    if form.is_valid():
        form.save()
        return redirect('/investors/')
    
    messages.info(request,"INVESTOR UPDATED SUCCESSFULLY!")

    context = {'investor':form}

    return render(request,"investors/investor_form.html",context)


def delete_investor(request,inv_id):
    selected_investor = investor.objects.get(id=inv_id)
    selected_investor.delete()
    messages.info(request,"INVESTOR DELETED SUCCESSFULLY!")
    return redirect('/investors/')


def add_inv_contact(request,inv_id):
    form = ContactForm()
    selected_investor = investor.objects.get(id=inv_id)
    if request.method == 'POST':
        form = InvestorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(InvestorDetail)
        messages.info(request,"CONTACT ADDED SUCCESSFULLY!")
    
    context = {
        'contact':form,
        'investor':selected_investor,
    }
    return render(request,"investors/investor_form.html",context)

def update_contact(request,contact_id):
    selected_contact = investor_contact.get(id=contact_id)
    form = ContactForm(instance = selected_contact)

    if request.method =="POST":
        form = ContactForm(request.POST, instance=selected_contact)

    if form.is_valid():
        form.save()
        return redirect("/")
    
    context = {
        'contact_form':form,
        }

    return render(request,"/",context)

def add_file(request,inv_id):
    form = FileForm()

    return render(request,InvestorDetail, {'form':form})
    
