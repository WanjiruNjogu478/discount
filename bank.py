

# default values
class BankAccount:
    def __init__(self, name="joyce", balance=50):
        self.name = name
        self.balance = balance

        print(f"my name is {self.name} and my bank balance is {self.balance}")

account = BankAccount()


class BankAccount:
    def __init__(self, name="joyce", balance=50):
        self.name = name
        self.balance = balance

        print(f"my name is {self.name} and my bank balance is {self.balance}")

defaultAccount = BankAccount()
print(defaultAccount.name)
print("----------------------------------------")
account = BankAccount("Ann", 70000)

# ENCAPSULATION
class BankAccount:
    def __init__(self, name="joyce", balance=50):
        self.name = name #public attribute
        self.__balance = balance #private attribute
        print(f"my name is {self.name} and my bank balance is {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

defaultAccount = BankAccount()
print(defaultAccount.name)
print(defaultAccount.get_balance())
print("----------------------------------------")
account = BankAccount("Ann", 70000)
account.deposit(45000)
print(f"After deposit, Balance {account.get_balance()}")
account.withdraw(12000)
print(f"After withdrawing, Balance: {account.get_balance()}")


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

        print(f"my name is {self.name} and my bank balance is {self.balance}")

acc = BankAccount("wanjiru", 5000000)


# ABSTRACTION

