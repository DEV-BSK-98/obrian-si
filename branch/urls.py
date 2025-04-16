from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="branch"),
    path ("info/<int:id>/", views.info, name="branch-info")
]