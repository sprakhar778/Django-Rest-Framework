from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import EmployeViewSet, ProjectViewSet


router=DefaultRouter()



router.register('employes',EmployeViewSet,basename='employes')
router.register('projects',ProjectViewSet,basename='projects')

employe_router=NestedDefaultRouter(router,'employes',lookup='employe')
employe_router.register('projects',ProjectViewSet,basename='employe-projects')



project_router=NestedDefaultRouter(router,'projects',lookup='project')
project_router.register('employes',EmployeViewSet,basename='project-employes')

urlpatterns=[
    path('',include(router.urls)),
    path('',include(employe_router.urls)),
    path('',include(project_router.urls)),
]