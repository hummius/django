from django.urls import path
from .views import blog_posts, published, user_posts


app_name = 'app_blogs'

urlpatterns = [
    path('blog-posts/', blog_posts, name='blog-posts'),
    path('post-pub/', published, name='post publish'),
    path('my-posts/', user_posts, name='my posts'),
]
