from django.shortcuts import render
from django.views.generic import FormView, CreateView
from .forms import *
from common.models import User

class Review(CreateView):
    form_class = ReviewForm
    template_name = 'write.html'
    success_url = "/"

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        login_session = self.request.session['user']
        writer = User.objects.get(email=login_session)
        temp_article.writer = writer
        temp_article.save()

        return super().form_valid(form)
