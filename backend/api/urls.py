from django.urls import path
from . import views

urlpatterns = [
    # -------- Vehicles --------
    path("vehicles/", views.VehicleListCreate.as_view(), name="vehicle-list"),
    path("vehicles/<int:pk>/", views.VehicleDetailView.as_view(), name="vehicle-detail"),

    # -------- Income --------
    path("income/", views.IncomeListCreateView.as_view(), name="income-list-create"),
    path("income/<int:pk>/", views.IncomeDetailView.as_view(), name="income-detail"),

    # -------- Expenses --------
    path("expenses/", views.ExpenseListCreateView.as_view(), name="expense-list-create"),
    path("expenses/<int:pk>/", views.ExpenseDetailView.as_view(), name="expense-detail"),
]