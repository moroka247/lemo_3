from django.urls import path
from . views import(
    InvestorList,
    InvestorDetail,
    add_investor,
    update_investor,
    delete_investor,
)

app_name = 'investors'

urlpatterns = [
    path('',InvestorList.as_view(),name='investors'),
    path('investor/<int:pk>/',InvestorDetail,name='detail'),
    path('add_investor',add_investor,name='add_investor'),
    path('update_investor/<int:inv_id>/',update_investor,name='update_investor'),
    path('delete_investor/<int:inv_id>/',delete_investor,name='delete_investor'),

]