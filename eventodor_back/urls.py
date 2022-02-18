from email.mime import base
from posixpath import basename
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, EventViewSet, OrgEventViewSet, OrganizationViewSet, OrganizerViewSet, PhotoViewSet, UserEventViewSet, UserViewSet, ReviewViewSet, FavouriteViewSet, CoordinateViewSet

router = SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('event', EventViewSet, basename='event')
router.register('eventuser', UserEventViewSet, basename='eventuser')
router.register('photo', PhotoViewSet, basename='photo')
router.register('review', ReviewViewSet, basename='review')
router.register('favourite', FavouriteViewSet, basename='favourite')
router.register('coordinate', CoordinateViewSet, basename='coordinate')
router.register('category', CategoryViewSet, basename='category')
router.register('organization', OrganizationViewSet, basename='organization')
router.register('organizer', OrganizerViewSet, basename='organizer')
router.register('orgevent', OrgEventViewSet, basename='orgevent')
# urlpatterns += router.urls
urlpatterns = router.urls