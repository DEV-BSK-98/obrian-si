from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="imports"),
    path ("pull", views.pull, name="import-item-pull"),
    path ("info/<int:id>/", views.info, name="import-item-info"),
]