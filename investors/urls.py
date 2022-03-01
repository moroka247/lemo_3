from django.urls import path
from . views import(
    InvestorList,
    investor_form,
    InvestorDetail,
    add_investor,
)

app_name = 'investors'

urlpatterns = [
    #path('',investors_home,name='investors'),
    path('',InvestorList.as_view(),name='investors'),
    #path('investor/<int:pk>',InvestorDetail.as_view(),name='detail'),
    path('investor/<int:pk>/',InvestorDetail,name='detail'),
    path('investor_form',investor_form,name='investor_form'), # add a new investor form or edit an existing one
    path('',add_investor,name='new_investor')
]