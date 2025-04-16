from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="item"),
    path ("info/<int:id>/", views.info, name="item-info")
]