from rest_framework import routers
from app_users.api import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
