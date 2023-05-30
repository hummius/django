from app_users.models import UserProfile
import logging


logger = logging.getLogger(__name__)


def reduce_balance(user_profile: UserProfile, check):
    user_profile.balance -= check
    user_profile.spenging_amount += check
    logger.info('Списание баллов с баланса')
    user_profile.save()
