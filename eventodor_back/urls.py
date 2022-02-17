from email.mime import base
from posixpath import basename
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import EventViewSet, PhotoViewSet, UserEventViewSet, UserViewSet

router = SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('event', EventViewSet, basename='event')
router.register('eventuser', UserEventViewSet, basename='eventuser')
router.register('photo', PhotoViewSet, basename='photo')
# urlpatterns += router.urls
urlpatterns = router.urls