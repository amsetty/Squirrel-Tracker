from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='sightings'),
    path('stats', views.stats, name ='stats')
]
