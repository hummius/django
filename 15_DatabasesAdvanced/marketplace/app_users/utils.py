from app_users.models import UserProfile


def reduce_balance(user_profile: UserProfile, check):
    user_profile.balance -= check
    user_profile.spenging_amount += check
    user_profile.save()
