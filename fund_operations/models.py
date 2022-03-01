from django.db import models
from funds.models import fund
from investors.models import investor
from investments.models import investment

# Create your models here.
class fund_close(models.Model):
    close_fund = models.ForeignKey(fund,on_delete=models.CASCADE,null=True)
    close_investor = models.ForeignKey(investor,on_delete=models.CASCADE,null=True)
    close_date = models.DateField(auto_now_add=False,auto_now=False)
    close_amount = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    def __str__(self):
        return str(self.close_fund) + " | " + str(self.close_investor)

class capital_call(models.Model):
    call_fund = models.ForeignKey(fund,on_delete=models.CASCADE,null=True)
    call_investor = models.ForeignKey(investor,on_delete=models.CASCADE,null=True)
    call_date = models.DateField(auto_now_add=False,auto_now=False)
    call_amount = models.DecimalField(max_digits=12,decimal_places=2,default=0)

    def __str__(self):
        return str(self.call_fund) + " | " + str(self.call_investor)

class disbursement(models.Model):
    disb_fund = models.ForeignKey(fund,on_delete=models.CASCADE,null=True)
    disb_investment = models.ForeignKey(investment,on_delete=models.CASCADE,null=True)
    disb_date = models.DateField(auto_now_add=False,auto_now=False)

    def __str__(self):
        return str(self.disb_fund) + " | " + str(self.disb_investment)

class distribution(models.Model):
    distr_fund = models.ForeignKey(fund,on_delete=models.CASCADE,null=True)
    distr_investor = models.ForeignKey(investor,on_delete=models.CASCADE,null=True)
    distr_date = models.DateField(auto_now_add=False,auto_now=False)
