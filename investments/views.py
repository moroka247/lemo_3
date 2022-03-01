from typing import ContextManager
from investments.models import investment
from django.views.generic import ListView, DetailView
from .models import investment, company

# Create your views here.

class InvestmentsList(ListView):
    model = investment
    template_name = 'investments/investments.html'
    context_object_name = 'investments'
    
class InvestmentDetail(DetailView):
    model = investment
    template_name = 'investments/investment_overview.html'

def InvestmentDetails(request,pk):
    selected_investment = investment.objects.get(id=pk)
    investment_company = company.objects.filter(co_name = selected_investment)

    Context = {
        'investment':selected_investment,
        'company':investment_company
    }

