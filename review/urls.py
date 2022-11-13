from django.contrib import admin
from django.urls import path

from review.views import *

urlpatterns = [
    path('write/', WriteReview.as_view(), name = 'write'),
    path('myreview/', MyReview.as_view(), name = 'myreview'),
    path("myreview/detail/<int:pk>/", DetailReview.as_view(), name="detail"),
    #path('map/', map, name = 'map'),
]