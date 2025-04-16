from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="purchases"),
    path ("info/<int:id>/", views.info, name="purchase-info")
]