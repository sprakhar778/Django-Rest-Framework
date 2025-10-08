# api/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
