"""bank_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from currency.views import get_rates, new_rate
from rest_framework.routers import DefaultRouter

from currency import views

router = DefaultRouter()
router.register('currency_rate', views.CurrencyRateViewSet)
router.register('student', views.StudentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/get_rates/', get_rates, name='get_rates'),
    # path('api/new_rate/', new_rate, name='new_rate'),
    path('api/currency_name/', views.CurrencyNameListCreate.as_view(), name='currency_name'),
    path('api/currency_name/<int:pk>/', views.CurrencyNameRetrieveUpdateDelete.as_view(), name='currency_detail'),
    path('api/', include(router.urls))
]
