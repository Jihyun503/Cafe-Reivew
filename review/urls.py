from django.contrib import admin
from django.urls import path

from review.views import *

urlpatterns = [
    path('write/', WriteReview.as_view(), name = 'write'),
    path('myreview/', MyReview.as_view(), name = 'myreview'),
    path('board/', ReviewBoard.as_view(), name = 'board'),
    path("myreview/detail/<int:pk>/", DetailReview.as_view(), name="detail"),
    path("board/detail/<int:pk>/", DetailReview.as_view(), name="detail"),
    path("myreview/modify/<int:pk>/", ModifyReview.as_view(), name="modify"),
    path("myreview/delete/<int:pk>/", deleteReview, name="delete"),
    #path("myreview/delete/<int:pk>/", DeleteReview.as_view(), name="delete"),
    #path('map/', map, name = 'map'),
]