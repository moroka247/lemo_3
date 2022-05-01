from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
from funds.models import fund
from instruments.models import instrument
from django.shortcuts import reverse

# Create your models here.

class industry(models.Model):
    industry_name = models.CharField(max_length=100)

    def __str__(self):
        return self.industry_name

class continent(models.Model):
    continent_name = models.CharField(max_length=50)

    def __str__(self):
        return self.continent_name

class country(models.Model):
    country_name = models.CharField(max_length=100)
    country_continent = models.ForeignKey(continent,on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.country_name

class perf_categories(models.Model):
    perf_status = models.CharField(max_length=25)
    Perf_status_descr = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = 'Perfomance Categories'

    def __str__(self):
        return self.perf_status

class company(models.Model):
    co_name = models.CharField(max_length=50)
    co_short_name = models.CharField(max_length=25,null=True)
    co_reg_no = models.CharField(max_length=50)
    co_description = models.TextField(max_length=200,null=True)
    co_industry = models.ForeignKey(industry,on_delete=models.DO_NOTHING,null=True)
    co_country = models.ForeignKey(country,on_delete=DO_NOTHING,null=True)

    def __str__(self):
        return self.co_name

class deal_stage(models.Model):
    stage_name = models.CharField(max_length=50)
    stage_description = models.TextField(max_length="200")

    def __str__(self):
        return self.stage_name

class investment(models.Model):
    inv_company = models.ForeignKey(company,on_delete=models.CASCADE)
    inv_fund = models.ForeignKey(fund,on_delete=models.CASCADE)
    inv_instrument = models.ForeignKey(instrument,on_delete=models.DO_NOTHING, null=True)
    inv_commitment = models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    inv_disbursed = models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    perf_status = models.ForeignKey(perf_categories,on_delete=models.CASCADE)
    inv_stage = models.ForeignKey(deal_stage,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.inv_company) + ' | ' + str(self.inv_fund)

    def get_absolute_url(self):
        return reverse('investments:detail', kwargs={'pk':self.pk})



