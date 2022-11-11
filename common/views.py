from django.shortcuts import render
from django.views.generic import CreateView 
from .forms import *

# Create your views here.

class SignUp(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = "/"
