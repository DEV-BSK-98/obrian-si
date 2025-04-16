from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="initialization"),
    path ("info", views.info, name="initialization-info")
]