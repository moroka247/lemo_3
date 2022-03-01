from django.urls import path
from .views import InvestmentsList, InvestmentDetail


app_name = 'funds'

urlpatterns = [
    path('',InvestmentsList.as_view(),name='investments'),
    path('investment/<int:pk>',InvestmentDetail.as_view(),name='detail'),
    path('investment_form',InvestmentDetail.as_view(),name='investment_form'),
]