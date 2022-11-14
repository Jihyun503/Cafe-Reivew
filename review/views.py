from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import *
from common.models import User
from .models import *
from common.decorators import login_required
from django.db.models import Q


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

class ReviewBoard(ListView):
    template_name = "reviews.html"
    #model = Review
    
    def get_queryset(self):
        qs = Review.objects.all()
        keyword = self.request.GET.get("keyword", None)
        search_type = self.request.GET.get("type", None)
        
        if keyword is not None:
            if search_type == 'all':
                qs = qs.filter(Q(shop_name__icontains=keyword)|Q(address__icontains=keyword)|Q(contents__icontains=keyword)|Q(writer__nickname__icontains=keyword))
            elif search_type == 'name':
                qs = qs.filter(shop_name__icontains=keyword)
            elif search_type == 'address':
                qs = qs.filter(address__icontains=keyword)
            elif search_type == 'content':
                qs = qs.filter(contents__icontains=keyword)
            elif search_type == 'writer':
                qs = qs.filter(writer__nickname__icontains=keyword)
            
        return qs
    

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
