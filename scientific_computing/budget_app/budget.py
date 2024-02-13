class Category:

	def __init__(self, name):
		"""
		initializes a new Category object with a name and an empty ledger

		args:
		- name: the name of the category

		attributes:
		- name: the name of the category
		- ledger: a list to store transactions
		"""
		self.name = name
		self.ledger = []

	def deposit(self, amount, description=""):
		"""
		adds a deposit transaction to the ledger

		args:
		- amount: the amount of the deposit
		- description: a description of the deposit

		returns:
		None
		"""
		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount, description=""):
		"""
		adds a withdrawal transaction to the ledger

		args:
		- amount: the amount of the withdrawal
		- description: a description of the withdrawal

		returns:
		True if the withdrawal was successful, False otherwise
		"""
		if self.check_funds(amount):
			self.ledger.append({"amount": -amount, "description": description})
			return True
		return False

	def get_balance(self):
		"""
		calculates the current balance of the category

		returns:
		the current balance
		"""
		return sum(item["amount"] for item in self.ledger)

	def transfer(self, amount, category):
		"""
		transfers funds from this category to another category

		args:
		- amount: the amount to transfer
		- category: the destination Category object

		returns:
		True if the transfer was successful, False otherwise
		"""
		if self.check_funds(amount):
			self.withdraw(amount, f"Transfer to {category.name}")
			category.deposit(amount, f"Transfer from {self.name}")
			return True
		return False

	def check_funds(self, amount):
		"""
		checks if there are sufficient funds for a transaction

		args:
		- amount: The amount to check

		returns:
		True if there are sufficient funds, False otherwise
		"""
		return amount <= self.get_balance()

	def __str__(self):
		"""
		returns a string representation of the category ledger

		returns:
		a string representation of the ledger
		"""
		title = f"{self.name:*^30}\n"
		items = "".join(f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
						for item in self.ledger)
		total = sum(item["amount"] for item in self.ledger)
		output = title + items + f"Total: {total}"
		return output


def create_spend_chart(categories):
	"""
	creates a bar chart showing the percentage spent by each category

	args:
	- categories: a list of Category objects

	returns:
	a string representing the bar chart
	"""
	# calculate the total amount spent and the percentage spent by each category
	spent = [
		sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
		for category in categories
	]
	total_spent = sum(spent)
	spent_percentage = [(amount / total_spent) * 100 for amount in spent]

	# create the bar chart string
	graph = "Percentage spent by category\n"
	for label in range(100, -1, -10):
		graph += f"{str(label).rjust(3)}| "
		for percentage in spent_percentage:
			graph += "o  " if percentage >= label else "   "
		graph += "\n"

	# add the category names below the chart
	graph += "    -" + "---" * len(categories) + "\n     "
	longest_name_length = max(len(category.name) for category in categories)
	for i in range(longest_name_length):
		for category in categories:
			graph += category.name[i] + "  " if len(category.name) > i else "   "
		if i < longest_name_length - 1:
			graph += "\n     "

	return graph