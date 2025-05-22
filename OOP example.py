import os
os.system('cls')



class BankAccount:
    bank_name = "TrustBank"

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance # protected attribute
        self.__transaction_id = 2000  # private attribute

    @classmethod
    def change_bankname(cls, new_name):
        cls.bank_name = new_name
        return f"The bank name has been changed into {cls.bank_name}"
    
    @staticmethod # for example id must be 4 digit
    def id_check(id):
        if len(id) != 4:
            return f"transaction id must be 4 digit."
        elif len(id) == 4:
            return f"you transaction id is valid"
    
    def __verify_transaction(self, given_id):  # private method
        return given_id == self.__transaction_id

    def show_balance(self):
        return f"{self.name}'s balance is ${self._balance}"

    def deposit(self, amount, transaction_id):
        # 👈 You need to call the private method here
        if not self.__verify_transaction(transaction_id):
            return ValueError("incorrect transaction ID, cannot continue")
        self._balance += amount
        return f"{self.name} balance is now ${self._balance} after deposit with ${amount} amount"

    def withdraw(self, amount, transaction_id):
        # 👈 Only allow if balance is enough
        if not self.__verify_transaction(transaction_id):
            return ValueError("incorrect transaction ID, cannot continue")
        if (self._balance < amount):
            return f"insufficient funds"
        self._balance -= amount
        print(f"{self.name} is withdrawing ${amount} amount of money")
        return f"this {self.name}'s current balance ${self._balance}"

    def transfer(self, to_account, amount, transaction_id):
        # 👈 Withdraw from self, deposit into to_account
        if not self.__verify_transaction(transaction_id):
            return ValueError("incorrect transaction ID, cannot continue")
        if (self._balance < amount):
            return f"insufficient funds"
        self._balance -= amount
        print(f"{self.name}'s balance is now {self._balance}")
        to_account._balance += amount
        print(f"transaction succeded")
        return f"{to_account.name}'s balance is now ${to_account._balance}"
    
    def __str__(self):
        return f"{self.name}'s balance is currently ${self._balance}"


acc1 = BankAccount("Alex", 1000)
acc2 = BankAccount("Peter", 3000)
acc3 = BankAccount("Mike", 1500)

print(acc2.show_balance())
print(acc1)
print(acc1.bank_name)
print(acc1.deposit(500,2000))
print(acc1.withdraw(500,2000))
print(acc2.transfer(acc1,1500,2000))
