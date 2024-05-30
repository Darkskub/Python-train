class Wallet:

    paymentSystem = "Visa"

    def __init__(self, name: str, currency: str, balance: float = 0):
        self.name = name
        self._balance = balance
        self.currency = currency

    def deposit(self, amount: float):
        self._balance += amount
        return self._balance  # Нужно для дебага

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


class CryptoWallet(Wallet):
    def __init__(self, name, currency, coin, balance=0):
        super().__init__(name, currency, balance)
        self.coin = coin

    def getBalance(self):
        return f"{self._balance} {self.coin}"

    def getBalanceInUsd(self):
        if self.coin == "BTC":
            return self._balance * 72000
        elif self.coin == "ETH":
            return self._balance * 3500
        else:
            return "Unknown coin"


a = CryptoWallet("Vic", "$", "ETH", 5000)

print(a.getBalance())
print(a.getBalanceInUsd())
