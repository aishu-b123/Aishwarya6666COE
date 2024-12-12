'''enter pin
1.validation
    1.deposit
    2.withdraw
    3.bal enquiry
    4.exit'''
class Bank:
    accBal=200000
    transaction_count = 0
    def deposit(self):
        amount=int(input("enter deposit amount:"))
        if amount<100:
            print("min deposit amount is 100")
        elif amount>50000:
            print("exceeded maximum amount 50000")
        else:
            if amount%100 !=0:
                print("enter the correct amount multiple of 100")
            else:
                self.accBal+=amount
                print("successful deposit,total balance:",self.accBal)
    def withdraw(self):
        if(self.transaction_count<3):
            amount=int(input('enter amount'))
            flag=True
            if amount> self.accBal:
                print("insufficient balance")
                flag=False
            if amount < 100:
                print("min amount is 100")
                flag = False
            if self.accBal-amount <500:
                print("need to maintain min 500 in account")
                flag = False
            if amount%100 !=0:
                print("enter the correct amount multiple of 100")
                flag = False
            if amount>20000:
                print("transaction amount limit exceeded")
                flag = False
            if flag:
                self.accBal-=amount
                self.transaction_count += 1
                print("balance:",self.accBal)
        if self.transaction_count==3:
            print("transactions limit completed")
    def bal(self):
        print(self.accBal)
    def show(self):
        opt=1
        while(opt!=0):
            print('1.deposit\n2.withdraw\n3.bal enquiry\n0.exit')
            opt=int(input('enter your option'))
            if opt==1:
                ob.deposit()
            elif opt==2:
                ob.withdraw()
            elif opt==3:
                ob.bal()
            else:
                print('enter correct option')
    def validate(self):
        count=0
        while(count<3):
            pin = int(input('enter password:'))
            if pin == 1234:
                ob.show()
                break
            else:
                count += 1
                print("invalid pin. try again")

ob=Bank()
ob.validate()