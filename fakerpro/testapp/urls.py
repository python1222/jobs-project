from django.urls import path
from testapp import views

urlpatterns = [
    path('',views.home),
    path('hydjobs/',views.hydjobsinfo),
    path('punejobs/',views.punejobsinfo),
    path('banglorejobs/',views.banglorejobsinfo),
]
