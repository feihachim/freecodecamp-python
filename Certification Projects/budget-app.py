"""
In this lab, you will build a simple budget app that tracks spending in different categories
and can show the relative spending percentage on a graph.
"""


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        transaction = {"amount": -amount, "description": description}
        self.ledger.append(transaction)
        return True

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction.get("amount")
        return balance

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        full_list = ""
        name_length = len(self.name)
        stars_number = (30 - name_length) // 2
        first_line = f"{stars_number * '*'}{self.name}{(30 - name_length - stars_number) * '*'}\n"
        full_list += first_line
        for transaction in self.ledger:
            if len(transaction.get("description")) <= 23:
                description = transaction.get("description")
            else:
                description = transaction.get("description")[0:23]
            amount = transaction.get("amount")
            amount = "{:.2f}".format(amount)
            space_number = 30 - len(str(amount)) - len(description)
            line = f"{description}{space_number * ' '}{amount}"
            full_list += line + "\n"
        total_line = f"Total: {self.get_balance()}"
        full_list += total_line
        return full_list


def create_spend_chart(categories):
    result = ""
    first_line = "Percentage spent by category"
    result += first_line
    spending_list = []
    for category in categories:
        pass
    return result


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)
