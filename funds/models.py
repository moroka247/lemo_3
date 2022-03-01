from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DecimalField
from django.shortcuts import reverse

from investors.models import investor

# Create your models here.

class f_structure(models.Model):
    f_structure = models.CharField(max_length=100)

    def __str__(self):
        return str(self.f_structure)

class currency(models.Model):
    name = models.TextField(max_length="30")   
    code = models.TextField(max_length="4")

    def __str__(self):
        return str(self.code)

class fund(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    objective = models.TextField(max_length=200, blank=True)
    investment_period = models.IntegerField(default=0,)
    divestment_period = models.IntegerField(default=0)
    life = models.IntegerField(default=0, null=True)
    target_commitment = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    commitment = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    drawn_capital = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    undrawn_capital = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    distributions = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    portfolio_count = models.IntegerField(default=0)
    man_fee = models.DecimalField(max_digits=3, default=0.00,decimal_places=2)
    structure = models.ForeignKey(f_structure,on_delete=models.DO_NOTHING,null=True)
    f_currency = models.ForeignKey(currency,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('funds:detail', kwargs={'pk':self.pk})

class f_close(models.Model):
    c_fund = models.ForeignKey(fund, on_delete=models.CASCADE,null=False)
    c_investor = models.ForeignKey(investor,on_delete=models.DO_NOTHING)
    c_amount = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    c_percentage = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    c_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.c_fund) + ' | ' + str(self.c_investor)