from django.urls import path

from app_users.views import (
    restore_password,
    register_view,
    user_account,
    AnotherLoginView,
    AnotherLogoutView,
    another_register_view,
    update_user_balance,
    users_order_history
)

urlpatterns = [
    path('register/', register_view, name='registration'),
    path('restore_password/', restore_password, name='restore_password'),
    path('account/', user_account, name='account'),
    path('login/', AnotherLoginView.as_view(), name='login'),
    path('logout/', AnotherLogoutView.as_view(), name='logout'),
    path('deposit/', update_user_balance, name='deposit'),
    path('orders-history/', users_order_history, name='orders-history')
]
