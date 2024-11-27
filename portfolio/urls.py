from django.urls import path
from .views import ProjectList, BlogList

urlpatterns = [
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('blog/', BlogList.as_view(), name='blog-list'),
]