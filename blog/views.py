from django.shortcuts import render
from .models import Post
def post_list(request):
    post = Post.objects.filter().order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts":post})
