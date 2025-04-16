from django.urls import path
from . import views

urlpatterns = [
    path ('', views.list_view, name="purchases"),
    path ('new-purchases', views.index, name="new-purchases"),
    path ('import-purchases', views.import_list_view, name="import-purchases"),
    path ("info/<int:id>/", views.info, name="purchase-info"),
    path ("import-purchase-info/<int:id>/", views.import_info, name="import-purchase-info"),
    path ("debit-note", views.list_debit_note, name="debit-note"),
    path ("debit-note-info", views.debit_note_info, name="debit-note-info"),
    path ("pull-purchases/", views.pull, name="pull-purchases"),
]