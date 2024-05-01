class Wallet:

    paymentSystem = "Visa"

    def __init__(self, name: str, currency: str, balance: float = 0):
        self.name = name
        self._balance = balance
        self.currency = currency

    def deposit(self, amount: float):
        self._balance += amount
        return self._balance # Нужно для дебага

    def pay(self, amount: float):
        if self._balance >= amount:
            self._balance -= amount
            return self._balance  # Нужно для дебага
        else:
            print("Insufficient funds")

    def getBalance(self):
        return f"{self._balance} {self.currency}"

    def delete(self):
        del self._balance
        del self.name
        del self.currency

a = Wallet("Vic", "$", 5000)

print(a.deposit(10))
print(a.pay(50))
print(a.pay(50000))
print(a.getBalance())
a.delete()
print(a.getBalance())