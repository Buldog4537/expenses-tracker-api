from django.contrib import admin
from .models import Income, Expenses, Categories, Budget


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("amount_display", "date")

    def amount_display(self, obj):
        return f"${obj.amount:,}"

    amount_display.short_description = "Amount"


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ("amount_display", "date")
