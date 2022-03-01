from django.contrib import admin
from .models import company, continent, country, industry, investment, perf_categories

# Register your models here.
admin.site.register(continent)
admin.site.register(country)
admin.site.register(industry)
admin.site.register(company)
admin.site.register(investment)
admin.site.register(perf_categories)
