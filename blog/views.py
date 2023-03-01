from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Post

# Create your views here.
def first_page(request):
    return render(request, 'blog/first_page.html')

def second_page(request):
    posts = Post.objects.all()
    return render(request, 'blog/second_page.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
