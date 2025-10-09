from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import UploadFileView,UploadFileDetailView
from .views import UploadFileView


router=DefaultRouter()

router.register('upload',UploadFileView,basename='upload')

urlpatterns=[
    path('',include(router.urls)),
]




# urlpatterns=[
#     path('upload/',UploadFileView.as_view(),name='upload'),
#     path('upload/<int:pk>/',UploadFileDetailView.as_view(),name='upload-detail'),
# ]