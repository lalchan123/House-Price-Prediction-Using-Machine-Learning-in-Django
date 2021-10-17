
from django.urls import path
from HousePredictionApp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('predict/result/', views.result, name='result'),
    path('predict/result/record', views.record, name='record'),
]