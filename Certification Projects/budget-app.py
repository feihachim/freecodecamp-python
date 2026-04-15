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

    def get_total_spendings(self):
        spendings = 0
        for transaction in self.ledger:
            amount = transaction.get("amount")
            if amount < 0:
                spendings += amount
        return abs(spendings)

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction.get("amount")
        return balance

    def transfer(self, amount, category: "Category"):
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


def get_spendings_rate_rounded_near_10(categories: list[Category]):
    spending_list = []
    for category in categories:
        name = category.name
        spending = category.get_total_spendings()
        item = {"name": name, "spending": spending}
        spending_list.append(item)
    total_spending = 0
    for expense in spending_list:
        total_spending += expense["spending"]
    for expense in spending_list:
        percentage = (((expense["spending"] / total_spending) * 100) // 10) * 10
        expense["percentage"] = percentage
    return spending_list


def right_align(num: int):
    word = str(num)
    l_num = len(word)
    if l_num == 2:
        word = f" {num}"
    if l_num == 1:
        word = f"  {num}"
    return word


def format_category_names(categories: list[Category]):
    max_length = 0
    for category in categories:
        if len(category.name) >= max_length:
            max_length = len(category.name)
    result = []
    for category in categories:
        name = f"{category.name}{(max_length - len(category.name)) * ' '}"
        result.append(name)
    return result


def create_spend_chart(categories: list[Category]):
    result = ""
    first_line = "Percentage spent by category\n"
    result += first_line
    spending_list = get_spendings_rate_rounded_near_10(categories)
    rate = 100
    first_part = ""
    while rate >= 0:
        first_part += f"{right_align(rate)}| "
        for spending in spending_list:
            if spending["percentage"] >= rate:
                first_part += "o  "
            else:
                first_part += "   "
        rate -= 10
        first_part += "\n"
    result += first_part
    second_part = f"    -{(3 * len(categories)) * '-'}\n"
    result += second_part
    last_part = ""
    formatted_names = format_category_names(categories)
    name_length = len(formatted_names[0])
    for i in range(name_length):
        last_part += "     "
        for name in formatted_names:
            last_part += f"{name[i]}  "
        last_part += "\n"
    result += last_part
    return result[:-1]


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(30, "cardigan")
print(food)
print("\n")
chart = create_spend_chart([food, clothing])
print(chart)
