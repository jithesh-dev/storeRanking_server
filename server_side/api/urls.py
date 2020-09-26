from django.urls import path
from . import views

urlpatterns = [
    path(r"get-store-data", views.StoreRanking.as_view(), name="getStoreData"),
]
