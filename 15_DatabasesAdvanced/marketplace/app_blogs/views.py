from django.shortcuts import render, redirect
from app_blogs.models import *
from app_users.models import UserProfile
from django.db import transaction
from django.http import HttpRequest, HttpResponse
from app_blogs.utils import reduce_user_balance, publish_post
from app_blogs.forms import PostForm


def blog_posts(request, *args, **kwargs):
    blog = Post.objects.select_related('blog').prefetch_related('authors').all()
    return render(request, 'app_blogs/blog-posts.html', {'posts_list': blog})


def user_posts(request, *args, **kwargs):
    posts = Post.objects.select_related('blog').prefetch_related('authors').filter(authors=request.user.id)
    return render(request, 'app_blogs/my-posts.html', {'posts_list': posts})

def publish_blog_post(post_id, user_id, scope_value):
    with transaction.atomic():
        reduce_user_balance(user_id, scope_value)
        publish_post(post_id)


def published(request: HttpRequest, *args, **kwargs):
    if request.method == 'POST':
        form = PostForm(request.POST)

        user_id = request.user.id
        print(user_id, 'user_id')
        profile = UserProfile.objects.get(user_id=user_id)
        print(profile, 'profile')
        post_id = request.post
        print(post_id, 'post_id')
        if profile.balance >= 1000:
            publish_blog_post(post_id, user_id, 1000)
            if form.is_valid():
                post = form.save()

                post.is_published = form.cleaned_data.get('is_published')
                post.save()

                return HttpResponse('Пост опубликован')
        else:
            return HttpResponse('Не хватает среств на балансе')

    post_form = PostForm()

    context = {
        'form': post_form
    }
    return render(request, 'app_blogs/post.html', context=context)
