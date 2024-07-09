from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.log, name='log'),
    path('log1', views.log1, name='log1'),
    path('log2', views.log2, name='log2'),
    path('signup1', views.signup1, name='signup1'),
    path('signup2', views.signup2, name='signup2'),
    path('result1', views.result1, name='result1'),
    path('result2', views.result2, name='result2')
]
