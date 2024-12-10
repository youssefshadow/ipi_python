class BankAccount:
    def __init__(self, name="John", balance=1000):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Montant de {amount} déposé sur le compte de {self.name}. Nouveau solde : {self.balance}")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Montant de {amount} retiré du compte de {self.name}. Nouveau solde : {self.balance}")
            else:
                print("Solde insuffisant pour effectuer le retrait.")
        else:
            print("Le montant du retrait doit être positif.")

    def display(self):
        print(f"Titulaire du compte : {self.name}, Solde : {self.balance}")


account1 = BankAccount()
account2 = BankAccount(name="Alice", balance=5000)

# Opérations sur compte 1
account1.display()
account1.deposit(500)
account1.withdraw(200)
account1.display()

# Opérations sur compte 2
account2.display()
account2.deposit(1000)
account2.withdraw(7000)
account2.withdraw(1000)
account2.display()
