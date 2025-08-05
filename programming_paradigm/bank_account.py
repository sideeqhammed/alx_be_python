class BankAccount:

  def __init__(self, initial_balance: 0):
    self.account_balance = initial_balance

  def deposit(self, amount):
    self.account_balance += amount
    return self.account_balance
  
  def withdraw(self, amount):
    balance = self.account_balance - amount
    if (balance >= 0):
      self.account_balance = balance
      return True
    else: 
      return False

  def display_balance(self):
    print(f"Current Balance: {self.account_balance}")
  
