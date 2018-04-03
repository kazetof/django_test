from django.shortcuts import render
from .models import Post
# from django.views.generic import DetailView

# Create your views here.
def blog(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'blog.html', {'posts': posts})

def post_details(request, post_id):
    post = Post(pk=post_id)
    return render(request, 'post.html', {'post':post})

# class PostDetailView(DetailView):
#     model = Post

#     def get_object(self, queryset=None):
#         post = super().get_object()
#         return post  