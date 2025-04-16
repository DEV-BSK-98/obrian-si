from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="sales"),
    path ("info/<int:id>/", views.info, name="sale-info")
]