class bank:
    def __init__(self,avilable_amount=0.0):
        self.balance=avilable_amount

    def log_trancation(self,trancation):
        with open('trancation.txt','a') as  file:
            file.write(f'{trancation} \t\t balance {self.balance}\n')

    def withdrawal(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount=0
        if amount:
         self.balance=self.balance-amount
         #return f'you have withdrawed amount {self.balance}'
        self.log_trancation(f'withdrew {amount}')
    
    def deposite(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount=0
        if amount:
            self.balance=self.balance+amount
            #return f'you have deposited amount {self.balance}'
        self.log_trancation(f'deposited {amount}')

account=bank(50.00)

while True:
    try:
     action=input("hello welcoming to banking withdrawal or deposite  :")
    except KeyboardInterrupt:
       print("your leaving the atm")
       break
    if action in ["withdrawal","deposite"]:
    
     if action == 'withdrawal':
      print('enter the amout you want to transact')
      amount = input("enter the amount: ")
      account.withdrawal(amount)
     
     else:
        print('enter the amout you want to transact')
        amount = input("enter the amount: ")
        account.deposite(amount)

     print(f"your balance is: {account.balance}")
    
    else:
       print("invalid option please enter valid options")
    


