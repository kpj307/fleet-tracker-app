from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from datetime import date, timedelta
from rest_framework import serializers
from django.db.models import Sum
from django.utils.timezone import now
from .models import Vehicle, Income, Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class VehicleSerializer(serializers.ModelSerializer):
    total_income = serializers.SerializerMethodField()
    total_expense = serializers.SerializerMethodField()
    profit = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "make",
            "plate",
            "total_income",
            "total_expense",
            "profit",
        ]

    def _date_filters(self):
        request = self.context.get("request")
        if not request:
            return {}

        period = request.query_params.get("period")
        start = request.query_params.get("start")
        end = request.query_params.get("end")

        today = date.today()

        # ✅ Explicit date range ALWAYS wins
        if start and end:
            return {
                "date__range": [
                    parse_date(start),
                    parse_date(end),
                ]
            }

        # 📅 Calendar Week (Mon–Sun)
        if period == "weekly":
            week_start = today - timedelta(days=today.weekday())
            week_end = week_start + timedelta(days=6)
            return {"date__range": [week_start, week_end]}

        # 📅 Calendar Month
        if period == "monthly":
            month_start = today.replace(day=1)
            if today.month == 12:
                next_month = today.replace(year=today.year + 1, month=1, day=1)
            else:
                next_month = today.replace(month=today.month + 1, day=1)

            return {"date__gte": month_start, "date__lt": next_month}

        # 📅 Calendar Year 
        if period == "annually":
            year_start = date(today.year, 1, 1)
            year_end = date(today.year, 12, 31)

            return {"date__range": [year_start, year_end]}

        # 📅 Custom (only if BOTH dates exist)
        if period == "custom" and start and end:
            return {
                "date__range": [
                    parse_date(start),
                    parse_date(end),
                ]
            }

        # 🚫 Custom with no dates → no filtering
        return {}

        
    def get_total_income(self, obj):
        return (
            Income.objects.filter(vehicle=obj, **self._date_filters())
            .aggregate(total=Sum("amount"))["total"]
            or 0
        )

    def get_total_expense(self, obj):
        return (
            Expense.objects.filter(vehicle=obj, **self._date_filters())
            .aggregate(total=Sum("amount"))["total"]
            or 0
        )

    def get_profit(self, obj):
        return self.get_total_income(obj) - self.get_total_expense(obj)

class IncomeSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=["%Y-%m-%d"])
    class Meta:
        model = Income
        fields = [
            "id",
            "vehicle",
            "amount",
            "date",
            "description",
        ]
        extra_kwargs = {
            "date": {"required": False}
        }


class ExpenseSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=["%Y-%m-%d"])
    class Meta:
        model = Expense
        fields = [
            "id",
            "vehicle",
            "amount",
            "date",
            "description",
            "category"
        ]
        extra_kwargs = {
            "date": {"required": False}
        }