from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="sars"),
    path ("info/<int:id>/", views.info, name="sar-info")
]