class account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def current_balance(self):
        return self.__balance

ac=account(name="",balance=1000)
print(ac.current_balance())
ac.deposit(50)
print(ac.current_balance())
ac.withdraw(10)
print(ac.current_balance())
