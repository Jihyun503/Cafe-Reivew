from django.contrib import admin
from django.urls import path

from common.views import *

urlpatterns = [
    path('join/', SignUp.as_view(), name = 'join'),
    path('login/', Login.as_view(), name = 'login'),
]