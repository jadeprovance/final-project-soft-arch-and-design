# comments/views.py

from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.urls import reverse 

def comment_list(request):
    comments = Comment.objects.all()
    form = CommentForm()
    return render(request, 'comments/comment_list.html', {'comments': comments, 'form': form})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(reverse('comments:comment_list'))
    else:
        form = CommentForm()
    return render(request, 'comments/comment_list.html', {'form': form})
