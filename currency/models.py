from django.utils import timezone
from django.db import models


class CurrencyName(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class CurrencyRate(models.Model):
    currency = models.ForeignKey(CurrencyName, on_delete=models.SET_NULL, null=True)
    rate = models.FloatField()
    currency_date = models.DateField(default=timezone.now)
    actual_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.currency.name} - {self.rate}'


class Student(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name