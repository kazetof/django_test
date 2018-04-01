from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'index.html', {'posts': posts})