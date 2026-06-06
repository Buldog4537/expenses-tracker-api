from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Income, Category, Expense, Budget


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ["id", "amount", "date", "user"]
        read_only_fields = ["user"]


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "amount", "date", "user", "category"]
        read_only_fields = ["user"]


class CategorySerializer(serializers.ModelSerializer):
    expenses = ExpenseSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "user", "expenses"]
        read_only_fields = ["user"]


class BudgetSerializer(serializers.ModelSerializer):
    amount_left = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = ["id", "user", "total", "amount_left"]
        read_only_fields = ["user"]

    def get_amount_left(self, obj):
        return obj.get_left()
