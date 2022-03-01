from django.contrib import admin
from .models import investor, investor_type, investor_contact

# Register your models here.
admin.site.register(investor)
admin.site.register(investor_type)
admin.site.register(investor_contact)
