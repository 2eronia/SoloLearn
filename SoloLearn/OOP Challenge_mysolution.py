class Account:

	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f"Owner: {self.owner} \nBalance: ${self.balance}"

	def __len__(self):
		return 30

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print("Deposit Accepted")
			print(f"Account Balance: ${self.balance}")

	def withdraw(self, amount):
		if amount > 0 and self.balance >= amount:
			self.balance -= amount
			print("Withdraw Accepted")
			print(f"Account Balance: ${self.balance}")
		else:
			print("Funds Unavalable")
			print(f"Account Balance: ${self.balance}")


# output
acct1 = Account('Serino', 100)
print("=" * 20)
print(acct1)
print(len(acct1))
print("=" * 20)
acct1.deposit(50)
print("=" * 20)
acct1.withdraw(75)
print("=" * 20)
acct1.withdraw(500)
