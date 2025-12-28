class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger: list[dict] = []

    def __str__(self):
        title = f"{self.name:*^30}\n"

        lines = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"

            lines += f"{description:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance():.2f}"

        return title + lines + total

    def deposit(self, amount, description=""):
        obj_deposit = {
            'amount': amount,
            'description': description
        }
        self.ledger.append(obj_deposit)

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount): return False

        obj_withdraw = {
            'amount': -amount,
            'description': description
        }
        self.ledger.append(obj_withdraw)
        return True

    def transfer(self, amount, category):
        if not self.check_funds(amount): return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def get_balance(self):
        return sum(entry["amount"] for entry in self.ledger) 

    def check_funds(self, amount):
        return self.get_balance() >= amount

def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    spent_per_category = []

    for category in categories:
        total_spent = 0
        for entry in category.ledger:
            amount = entry["amount"]
            if amount < 0:
                total_spent += -amount
        spent_per_category.append(total_spent)

    total_spent_all = sum(spent_per_category)

    percentages = [
        int((amount / total_spent_all) * 100) // 10 * 10
        for amount in spent_per_category
    ]

    chart = title

    for level in range(100, -10, -10):
        chart += f"{level:>3}| "
        for p in percentages:
            chart += "o  " if p >= level else "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            char = name[i] if i < len(name) else " "
            chart += char + "  "
        if i < max_len - 1:
            chart += "\n"

    return chart
