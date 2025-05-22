import os
os.system('cls')



class BankAccount:
    Bank_name   =   "RBA"
    def __init__(self, name, PIN, money):
        self.name       =   name
        self.__PIN      =   PIN
        self._money     =   money
    
    def __logic__(self, other, op):
        if not isinstance(other, BankAccount):
            raise ValueError("value is not an object/instance, cannot continue")
        if op == 'eq':
            return self.value == other.value
        elif op == 'lt':
            return self.value < other.value
        elif op == 'gt':
            return self.value > other.value
        elif op == 'add':
            return self.value + other.value
        elif op == 'sub':
            return self.value - other.value
    def __eq__(self, other):
        return self.__logic__(other,'eq')
    def __lt__(self,other):
        return self.__logic__(other,'lt')
    def __gt__(self,other):
        return self.__logic__(other,'gt')
    def __add__(self,other):
        return self.__logic__(other,'add')
    def __sub__(self,other):
        return self.__logic__(other,'sub')
    def __str__(self):
        return f"{self.name}, {self.__PIN}, {self._money}"
    def __repr__(self):
        return f"BankAccount(\"{self.name}\", \"{self.__PIN}\", {self._money})"
    
    @classmethod
    def acc_stat(cls):
        if cls==BankAccount:
            return f"Your account is a standard account." 
        elif cls==Premium:
            return f"Your account is a premium account."
        
    @staticmethod
    def acc_fee(value):
        # transaction fee, deposit fee, withdrawal fee, etc.
        # fee is 50
        value = value - 50
        return value
    
    def validation(self, PIN, amount):
        if not self.__PIN==PIN:
            raise ValueError("wrong PIN")
        if not type(self.__PIN)==int:
            raise ValueError("PIN must be integers")
        if not len(str(self.__PIN))==6:
            raise ValueError("PIN must be 6 digit")
        if amount < 0:
            raise ValueError("insufficient amount")
        return True

    def deposit(self, PIN, amount):
        self.validation(PIN, amount)
        if amount > 5000:
            raise ValueError("must be a premium account!")
        self._money += amount
        self._money = BankAccount.acc_fee(self._money)
        print(f"your current amount is {self._money}$")
        return f"money deposited successfully."
    def withdraw(self, PIN, amount):
        self.validation(PIN, amount)
        if amount > 5000:
            raise ValueError("must be a premium account!")
        if self._money < amount:
            raise ValueError("insufficient amount!")
        self._money -= amount
        self._money = BankAccount.acc_fee(self._money)
        print(f"successfully withdrawed {amount}")
        return f"money withdrawed successfully"
    def send_money(self, other, PIN, amount):
        self.validation(PIN, amount)
        if amount > 5000:
            raise ValueError("must be a premium account!")
        if self._money < amount:
            raise ValueError("insufficient amount!")
        self._money -= amount
        other._money += amount
        self._money = BankAccount.acc_fee(self._money)
        self.validation(PIN, self._money)
        return f"transaction successfull"
    def money_check(self, PIN):
        self.validation(PIN, self._money)
        print(f"Name: {self.name}")
        print(f"Your current balance is {self._money}$")
        return f"Thank you for using our services."

class Premium(BankAccount):
    def __init__(self, name, PIN, money):
        super().__init__(name, PIN, money)

    @classmethod
    def acc_stat(cls):
        return super().acc_stat()
    
    def deposit(self, PIN, amount):
        self.validation(PIN, amount)
        self._money += amount
        self._money = BankAccount.acc_fee(self._money)
        print(f"your current amount is {self._money}$")
        return f"money deposited successfully."
    def withdraw(self, PIN, amount):
        self.validation(PIN, amount)
        if self._money < amount:
            raise ValueError("insufficient amount!")
        self._money -= amount
        self._money = BankAccount.acc_fee(self._money)
        print(f"successfully withdrawed {amount}")
        return f"money withdrawed successfully"
    def send_money(self, other, PIN, amount):
        self.validation(PIN, amount)
        if self._money < amount:
            raise ValueError("insufficient amount!")
        self._money -= amount
        other._money += amount
        self._money = BankAccount.acc_fee(self._money)
        self.validation(PIN, self._money)
        return f"transaction successfull"
    def money_check(self, PIN):
        self.validation(PIN, self._money)
        print(f"Name: {self.name}")
        print(f"You are a premium member.")
        print(f"Your current balance is {self._money}$")
        return f"Thank you soo much for using our services!!"
    
acc1 = BankAccount("Peter",123456,1000)
acc2 = BankAccount("Lukas",121212,2000)

acc3 = Premium("Bartholomew",242424,30000)
acc4 = Premium("Jeffreyson",363636,20000)

print(acc1.deposit(123456,1500))
print('\n')
print(acc1.send_money(acc2,123456,1000))
print('\n')
print(acc1.withdraw(123456,400))
print('\n')
print(acc1.money_check(123456))
print(15*'-',"social gap",15*'-')
print(acc3.deposit(242424,6500))
print('\n')
print(acc3.send_money(acc4,242424,7500))
print('\n')
print(acc3.withdraw(242424,6000))
print('\n')
print(acc3.money_check(242424))
print('\n')
print(acc4.money_check(363636))
