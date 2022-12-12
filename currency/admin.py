from django.contrib import admin

from .models import CurrencyName, CurrencyRate

admin.site.register(CurrencyRate)
admin.site.register(CurrencyName)