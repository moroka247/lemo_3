from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from .models import fund, f_close
from .forms import FundForm
from django.views.generic import ListView, UpdateView, CreateView

# Create your views here.

class FundsList(ListView):
    model = fund
    template_name = 'funds/funds.html'
    context_object_name = 'funds'

def FundDetail(request,pk):
    selected_fund = fund.objects.get(id=pk)
    fund_close = f_close.objects.filter(c_fund = selected_fund)

    context = {
        'fund': selected_fund,
        'close_records': fund_close
    }
    return render(request,'funds/fund_overview.html', context)

class UpdateFund(UpdateView):
    model = fund
    form_class = FundForm
    template_name = 'funds/fund_form.html'
    success_url = '/funds/'

#def funds_home(request):
#    funds = fund.objects.all()
#    return render(request,'funds/funds.html', {'funds':funds})

#def fund_detail(request,**kwargs):
#    pk = kwargs.get('pk')
#    f = fund.objects.get(pk=pk)
#    return render(request, 'funds/fund_detail.html',{'fund':f})

class AddFund(CreateView):
    model = fund
    form_class = FundForm
    template_name = 'funds/add_fund.html'
    context_object_name = 'fund'
    success_url = '/funds/'

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Fund has been added'
        )

        return super().form_valid(form)

def fund_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = FundForm()
        else:
            selected_fund = fund.objects.get(pk=id)
            form = FundForm(instance=selected_fund)

        return render(request,"funds/fund_form.html",{'fund':form})
    else:
        if id==0:
            form = FundForm(request.POST)
        else:
            selected_fund = fund.objects.get(pk=id)
            form = FundForm(request.POST, instance=selected_fund)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.life += instance.investment_period
            instance.life += instance.divestment_period
            print("Valid")
            instance.save()
            return redirect('/funds/')

def delete_fund(request,id):
    selected_fund = fund.objects.get(pk=id)
    selected_fund.delete()
    return redirect ('funds.html')