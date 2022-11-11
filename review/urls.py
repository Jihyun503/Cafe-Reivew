from django.contrib import admin
from django.urls import path

from review.views import *

urlpatterns = [
    path('write/', Review.as_view(), name = 'write')
    #path('map/', map, name = 'map'),
]