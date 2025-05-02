from rest_framework.routers import DefaultRouter
from trends.viewset import TrendViewSet


router = DefaultRouter()

router.register('trends', TrendViewSet, basename='trends')


url_patterns = router.urls