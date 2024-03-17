class Account:
    def __init__(self):
        self.balance=0
        print('Hello!!Welcome to the Deposit and Withdrawal MAchine!!')
    def deposit(self):
        amount=float(input('Enter the amount to be deposited:'))
        self.balance+=amount 
        print('\nAmount deposited:',amount)
    def withdraw(self):
        amount=float(input('Enter amount to be withdrawan:'))
        if self.balance>=amount:
            self.balance-=amount 
            print('\nYou withdrew:',amount)
        else: 
            print('\nInsufficient balance.')
    def display(self):
        print('\nNet available balance=',self.balance)
class Customer(Account):
    def __init__(self):
        super().__init__()
        self.name=input('Enter your name:')
        print('Hello! Welcome!',self.name)
    def display(self):
        print('My name is',self.name)
        super().display()
#driver code 
c1 = Customer()
c1.deposit()
c1.Withdrawal()
c1.display()

c2 = Customer()
c2.deposit()
c2.Withdrawal()
c2.display()
