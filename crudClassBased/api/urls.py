from django.urls import path
from .views import CrudView


urlpatterns = [
    path("blogs/",CrudView.as_view()),
    path("blogs/<int:pk>/",CrudView.as_view()),
]