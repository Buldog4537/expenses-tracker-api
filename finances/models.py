from django.db import models
from django.db.models import Sum


class Income(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Income: {self.amount}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Expense: {self.amount}"


class Budget(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"Budget: {self.total}"

    def get_left(self):
        total_expenses = (
            Expense.objects.filter(user=self.user).aggregate(total=Sum("amount"))[
                "amount__sum"
            ]
            or 0
        )

        return self.total - total_expenses
