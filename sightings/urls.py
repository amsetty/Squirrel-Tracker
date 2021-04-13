from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name='sightings'),
    re_path('add',views.add, name ='add'),
    path('stats', views.stats, name ='stats'),
    re_path('^(?P<unique_squirrel_id>[\w-]+)$',views.update)
]
