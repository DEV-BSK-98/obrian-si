from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="imports"),
    path ("info/<int:id>/", views.info, name="import-item-info")
]