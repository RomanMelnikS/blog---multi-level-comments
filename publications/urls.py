from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PublicationsViewSet

router_v1 = DefaultRouter()
router_v1.register(
    r'publications',
    PublicationsViewSet,
    basename='publications'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]