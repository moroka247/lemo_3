from typing import ContextManager
from investments.models import investment
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import investment, company
from .forms import CompanyForm, InvestmentForm
from django.contrib import messages

# Create your views here.

class InvestmentsList(ListView):
    model = investment
    template_name = 'investments/investments.html'
    context_object_name = 'investments'
    
class InvestmentDetail(DetailView):
    model = investment
    template_name = 'investments/investment_overview.html'

def create_company(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investments/deal_form.html/')
        messages.info(request,"COMPANY ADDED SUCCESSFULLY!")
    
    context = {
        'deal':form,
    }
    return render(request,"investments/company_form.html",context)

def add_deal(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investments/deal_form.html/')
        messages.info(request,"COMPANY ADDED SUCCESSFULLY!")
    
    context = {
        'deal':form,
    }
    return render(request,"investments/deal_form.html",context)

    
def update_investment(request,inv_id):
    selected_investment = investment.objects.get(id=inv_id)
    form = InvestmentForm(instance = selected_investment)

    if request.method =="POST":
        form = InvestmentForm(request.POST, instance=selected_investor)

    if form.is_valid():
        form.save()
        return redirect('/investments/')
    
    context = {'investment':form}

    return render(request,"investments/deal_form.html",context)


def delete_investment(request,inv_id):
    selected_investment = investment.objects.get(id=inv_id)
    selected_investment.delete()
    messages.info(request,"INVESTMENT DELETED SUCCESSFULLY!")
    return redirect('/investments/')
