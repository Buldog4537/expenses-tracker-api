from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Income, Category, Expense, Budget
from .serializers import (
    IncomeSerializer,
    CategorySerializer,
    ExpenseSerializer,
    BudgetSerializer,
)


class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()

    serializer_class = IncomeSerializer

    permission_classes = [IsAuthenticated]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticated]


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()

    serializer_class = ExpenseSerializer

    permission_classes = [IsAuthenticated]


class BudgetViewSEt(ModelViewSet):
    queryset = Budget.objects.all()

    serializer_class = BudgetSerializer

    permission_classes = [IsAuthenticated]
