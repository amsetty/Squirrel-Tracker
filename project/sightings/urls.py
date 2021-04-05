from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name='sightings'),
    re_path('^(?P<unique_squirrel_id>[\w-]+)$',views.update)
]
