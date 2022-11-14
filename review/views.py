from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import *
from common.models import User
from .models import *
from common.decorators import login_required


class WriteReview(CreateView):
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

class MyReview(ListView):
    template_name = "myreview.html"
    model = Review

class DetailReview(DetailView):
    template_name = "detail.html"
    model = Review

class ModifyReview(UpdateView):
    template_name = "modify.html"
    model = Review
    form_class = ReviewForm
    success_url = '/'

def deleteReview(request, pk):
    board = get_object_or_404(Review, bno=pk)
    board.delete()

    return redirect('/review/myreview')
