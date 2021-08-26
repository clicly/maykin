from django.contrib import admin
from django.urls import path

from back.views import CityList

urlpatterns = [
    path('list/', CityList.as_view(), name='city_list'),

]
