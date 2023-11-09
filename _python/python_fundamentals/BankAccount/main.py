class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
      
        self.int_rate = int_rate  
        self.balance = balance    

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
        return self  

    def withdraw(self, amount):
        
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print(" invalid amount for withdrawal")
        return self  

    def display_account_info(self):
  
        print(f"Balance:{self.balance}, Interest Rate: {self.int_rate * 100}")
        return self  

    def yield_interest(self):
      
        self.balance += self.balance * self.int_rate
        return self  


account1 = BankAccount() 
account2 = BankAccount(0.02, 1000)  

account1.deposit(100).deposit(200).withdraw(50).yield_interest().display_account_info()
account2.deposit(500).deposit(300).withdraw(200).yield_interest().display_account_info()

