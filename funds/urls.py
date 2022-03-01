from django.urls import path
from . views import(
    FundsList,
    FundDetail,
    AddFund,
    UpdateFund,
    fund_form,
    delete_fund,
) 

app_name = 'funds'

urlpatterns = [
    path('',FundsList.as_view(),name='funds'),
    path('funds/<int:pk>',FundDetail,name='detail'),
    path('add',AddFund.as_view(),name='add_fund'),
    path('funds/edit',UpdateFund.as_view(),name='update_fund'),
    path('fund_form',fund_form,name='fund_form'), # add a new fund form or edit an existing one
    path('delete/<int:id>/',delete_fund,name='delete_fund'), # delete a fund
    
]