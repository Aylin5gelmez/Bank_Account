class Bank:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("An amount of {} $ has been deposited into your account.".format(amount))
        else:
            print("Your transaction has been suspended, invalid amount.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("An amount of {} $ has been withdrawn from your account.".format(amount))
        else:
            print("Insufficient balance.")
    
    def display_balance(self):
        print("The balance of your {} account is: {} $.".format(self.account_holder, self.balance))

    
account1 = Bank("Aylin GELMEZ", 800)  
account2 = Bank("Paul WALKER", 750)

account1.deposit(400)
account1.withdraw(600)
account1.display_balance()

print("\n")

account2.deposit(200)
account2.withdraw(1000)
account2.display_balance()
