from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, CategoryViewSet, ExpenseViewSet, BudgetViewSet

router = DefaultRouter()

router.register("incomes", IncomeViewSet)
router.register("categories", CategoryViewSet)
router.register("expenses", ExpenseViewSet)
router.register("budgets", BudgetViewSet)
