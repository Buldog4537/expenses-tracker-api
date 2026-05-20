from django.contrib import admin
from .models import Income, Expense, Category, Budget


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("user", "amount_display", "date")

    def amount_display(self, obj):
        return f"${obj.amount:,}"

    amount_display.short_description = "Amount"


@admin.register(Expense)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "category", "date")
    list_filter = ("user", "category", "date")
    search_fields = ("user__username",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("user", "total_display", "spent_display", "left_display")

    def total_display(self, obj):
        return f"${obj.total:,}"

    total_display.short_description = "Total"

    def spent_display(self, obj):
        spent = obj.total - obj.get_left()
        return f"${spent:,}"

    spent_display.short_description = "Spent"

    def left_display(self, obj):
        return f"${obj.get_left():,}"

    left_display.short_description = "Remaining"
