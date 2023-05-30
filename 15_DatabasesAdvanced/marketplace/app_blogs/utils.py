from app_users.models import UserProfile


def reduce_user_balance(user, value):
    user.userprofile.balance -= value
    user.userprofile.balance.save()


def publish_post(post):
    post.is_published = True
