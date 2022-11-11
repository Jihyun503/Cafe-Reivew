from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from .forms import *

# Create your views here.

class SignUp(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = "/"

class Login(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = "/"
    
    def form_valid(self, form):
        self.request.session['user'] = form.email

        return super().form_valid(form)

def logout(request):
    request.session.flush()
    return redirect('/')