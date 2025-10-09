from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UploadFileView


router=DefaultRouter()

router.register('upload',UploadFileView,basename='upload')

urlpatterns=[
    path('',include(router.urls)),
]