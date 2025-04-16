from django.urls import path
from . import views

urlpatterns = [
    path ('', views.list, name="branch"),
    path ('new-branch', views.index, name="new-branch"),
    path ("info/<int:id>/", views.info, name="branch-info")
]