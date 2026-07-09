from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IncomeViewSet,
    CategoryViewSet,
    ExpenseViewSet,
    BudgetViewSet,
)

router = DefaultRouter()

router.register("incomes", IncomeViewSet, basename="income")
router.register("categories", CategoryViewSet, basename="category")
router.register("expenses", ExpenseViewSet, basename="expense")
router.register("budgets", BudgetViewSet, basename="budget")

urlpatterns = [
    path("", include(router.urls)),
]
