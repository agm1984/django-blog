from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def starting_page(request):
    lastest_posts = Post.objects.all().order_by('-date')[:3]

    return render(request, 'blog/index.html', {
        'posts': lastest_posts,
    })


def posts(request):
    all_posts = Post.objects.all().order_by('-date')

    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts,
    })


def single_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'tags': identified_post.tags.all(),
    })