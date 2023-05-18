from django.shortcuts import render
from .models import Post
from .models import Comments


def home(request):
    context = {
        'posts': Post.objects.all(),
        'comments': Comments.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
