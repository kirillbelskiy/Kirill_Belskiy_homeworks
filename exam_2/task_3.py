class Client:
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id

class BankAccount:
    def __init__(self, account_number, initial_balance, client):
        self.account_number = account_number
        self.balance = initial_balance
        self.client = client

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств на счете")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        account_number = len(self.accounts) + 1
        account = BankAccount(account_number, initial_balance, client)
        self.accounts[account_number] = account
        return account_number

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, sender_account, receiver_account, amount):
        sender = self.get_account(sender_account)
        receiver = self.get_account(receiver_account)
        if sender and receiver:
            sender.withdraw(amount)
            receiver.deposit(amount)
        else:
            raise ValueError("Счет не существует")

    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client == client:
                total_balance += account.balance
        return total_balance



bank = Bank()

client1 = Client("Иванов Иван", 1)
client2 = Client("Петров Петр", 2)

account1 = bank.create_account(client1, 1000)
account2 = bank.create_account(client1, 2000)
account3 = bank.create_account(client2, 1500)

bank.get_account(account1).deposit(500)
bank.get_account(account2).deposit(1000)
bank.get_account(account3).deposit(800)

try:
    bank.get_account(account1).withdraw(300)
    bank.get_account(account2).withdraw(700)
    bank.get_account(account3).withdraw(200)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    bank.transfer(account1, account3, 200)
except ValueError as e:
    print(f"Ошибка: {e}")

total_balance_client1 = bank.get_total_balance(client1)
total_balance_client2 = bank.get_total_balance(client2)

print(f"Общий баланс клиента {client1.name}: {total_balance_client1}")
print(f"Общий баланс клиента {client2.name}: {total_balance_client2}")
