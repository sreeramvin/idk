from rest_framework import routers
from .api import UsersViewSet
from .views import Table

router = routers.DefaultRouter()
router.register('api/users', UsersViewSet, 'users')


urlpatterns = router.urls
