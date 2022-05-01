from django.urls import path
from .views import (
    InvestmentsList, 
    InvestmentDetail,
    add_deal,
    create_company,
    update_investment,
    delete_investment,
)

app_name = 'funds'

urlpatterns = [
    path('',InvestmentsList.as_view(),name='investments'),
    path('investment/<int:pk>',InvestmentDetail.as_view(),name='detail'),
    path('investment_form',InvestmentDetail.as_view(),name='investment_form'),
    path('create_company',create_company,name='create_company'),
    path('add_deal',add_deal,name='add_deal'),
    path('update_investment/<int:inv_id>/',update_investment,name='update_investment'),
    path('delete_investment/<int:inv_id>/',delete_investment,name='delete_investment'),
]