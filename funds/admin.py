from django.contrib import admin
from .models import (
    currency,
    f_close,
    fund,
    f_structure,
#    currency
)
# Register your models here.
admin.site.register(fund)
admin.site.register(f_structure)
admin.site.register(f_close)
admin.site.register(currency)
