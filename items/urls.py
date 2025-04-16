from django.urls import path
from . import views

urlpatterns = [
    path ('', views.list, name="items"),
    path ('new-item', views.index, name="new-item"),
    path ("info/<int:id>/", views.info, name="item-info")
]