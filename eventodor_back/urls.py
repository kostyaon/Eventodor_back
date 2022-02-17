from posixpath import basename
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import EventViewSet, UserViewSet

router = SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('event', EventViewSet, basename='event')
urlpatterns = router.urls