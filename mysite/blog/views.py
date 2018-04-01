from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'blog.html', {'posts': posts})