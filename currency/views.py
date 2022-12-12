import json
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework import viewsets

from .models import CurrencyName, CurrencyRate, Student
from .serializers import CurrencyRateSerializer, CurrencyNameSerializer, StudentSerializer


class CurrencyNameListCreate(generics.ListCreateAPIView):
    queryset = CurrencyName.objects.all()
    serializer_class = CurrencyNameSerializer


class CurrencyNameRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CurrencyName.objects.all()
    serializer_class = CurrencyNameSerializer


class CurrencyRateViewSet(viewsets.ModelViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# def get_rates(request):
#     rates = CurrencyRate.objects.all()
#     data = []
#     for rate in rates:
#         obj = {'currency': rate.currency.name, 'value': rate.rate}
#         data.append(obj)
#     return HttpResponse(json.dumps(data))

#
# def new_rate(request):
#     name = request.GET.get('name')
#     value = request.GET.get('value')
#     rate_name = CurrencyName.objects.get(name=name)
#     rate = CurrencyRate.objects.create(currency=rate_name, rate=float(value))
#     obj = {'currency': rate.currency.name, 'value': rate.rate}
#     return HttpResponse(json.dumps(obj))
