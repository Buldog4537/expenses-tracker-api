from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from .models import Expense, Category

User = get_user_model()


class ExpenseTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="pass123")

        self.category = Category.objects.create(user=self.user, name="Food")

        self.client.login(username="user1", password="pass123")

    def test_create_expense(self):
        response = self.client.post(
            "/finances/expenses/", {"amount": 50, "category": self.category.id}
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Expense.objects.count(), 1)

    def test_expense_list_authenticated(self):
        response = self.client.get("/finances/expenses/")
        self.assertEqual(response.status_code, 200)
