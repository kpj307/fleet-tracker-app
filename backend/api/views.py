from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from rest_framework import generics
from .serializers import UserSerializer, VehicleSerializer, IncomeSerializer, ExpenseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Vehicle, Income, Expense

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class VehicleListCreate(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Vehicle.objects.filter(owner=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        else:
            print(serializer.errors)

class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.filter(owner=self.request.user)

class IncomeListCreateView(generics.ListCreateAPIView):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        vehicle_id = self.request.query_params.get("vehicle")
        start = self.request.query_params.get("start")
        end = self.request.query_params.get("end")

        qs = Income.objects.filter(vehicle__owner=self.request.user)

        if vehicle_id:
            qs = qs.filter(vehicle_id=vehicle_id)  

        if start and end:
            qs = qs.filter(
                date__gte=parse_date(start),
                date__lte=parse_date(end)
            )

        return qs.order_by("-date")

    def perform_create(self, serializer):
        serializer.save()

class IncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # user can only edit/delete their own entries
        return Income.objects.filter(vehicle__owner=self.request.user)


class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        vehicle_id = self.request.query_params.get("vehicle")
        start = self.request.query_params.get("start")
        end = self.request.query_params.get("end")

        qs = Expense.objects.filter(vehicle__owner=self.request.user)

        if vehicle_id:
            qs = qs.filter(vehicle_id=vehicle_id)  

        if start and end:
            qs = qs.filter(
                date__gte=parse_date(start),
                date__lte=parse_date(end)
            )

        return qs.order_by("-date")

    def perform_create(self, serializer):
        serializer.save()

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # user can only edit/delete their own entries
        return Expense.objects.filter(vehicle__owner=self.request.user)
