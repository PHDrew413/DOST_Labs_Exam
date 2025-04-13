from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LabsViewSet

router = DefaultRouter()
router.register(r'labs', LabsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
