import unittest


class Expense:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def display_expense(self):
        print(f"Amount: ${self.amount:.2f}")
        print(f"Description: {self.description}")


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        return total

    def display_all_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        for i, expense in enumerate(self.expenses):
            print(f"\n--- Expense {i + 1} ---")
            expense.display_expense()

class TestExpenseTracker(unittest.TestCase):
    def test_add_expense(self):
        tracker = ExpenseTracker()
        expense = Expense(10, "Test Expense")
        tracker.add_expense(expense)
        self.assertIn(expense, tracker.expenses)

    def test_get_total_expenses(self):
        tracker = ExpenseTracker()
        expense1 = Expense(10, "Expense 1")
        expense2 = Expense(25, "Expense 2")
        tracker.add_expense(expense1)
        tracker.add_expense(expense2)
        total = tracker.get_total_expenses()
        self.assertEqual(total, 35)


def main():
    unittest.main()


if __name__ == "__main__":
    main()