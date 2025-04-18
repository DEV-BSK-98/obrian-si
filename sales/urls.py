from django.urls import path
from . import views

urlpatterns = [
    path ('', views.sales_list, name="sales"),
    path ("info/<int:id>/", views.info, name="sale-info"),
    path ('sale-new', views.index, name="sale-new"),
    path ('credit-note', views.credit_note_list, name="credit-note"),
    path ('credit-new-note', views.credit_note_new, name="credit-new-note"),
    path ("credit-note/<int:id>/", views.credit_note_info, name="credit-note-info")
]