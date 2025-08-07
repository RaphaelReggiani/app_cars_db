from rest_framework.routers import DefaultRouter
from .api_views import CarsViewSet, CardataViewSet, NewUserViewSet

router = DefaultRouter()
router.register(r'cars', CarsViewSet)
router.register(r'cardata', CardataViewSet)
router.register(r'users', NewUserViewSet)

urlpatterns = router.urls
