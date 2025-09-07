from django.urls import path
from .views import CustomerRegisterView, CustomerListView

urlpatterns = [
    path("register/", CustomerRegisterView.as_view(), name="customer-register"),
    path("customers/", CustomerListView.as_view(), name="customer-list"),
]
