from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post, Category, Comment


# def blog_index(request):
#     posts = Post.objects.all().order_by('created_at')
#     return render(request, 'blog/blog_index.html', {'posts': posts})


class LBlogView(ListView):
    model = Post
    template_name = 'blog/blog_index.html'
    # queryset = Post.objects.all().order_by('-created_at')
    def get_queryset(self):
        posts = Post.objects.all().order_by('-created_at').filter(pk__in=[1,3])
        return posts


# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     comments = Comment.objects.filter(post=post)
#     context = {'post': post, 'comments': comments}
#     return render(request, 'blog/blog_detail.html', context=context)


class DetailBlogView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('created_at')
    context = {'posts': posts, 'category': category}
    return render(request, 'blog/blog_category.html', context=context)
