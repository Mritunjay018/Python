class bankaccount:
    count = 100 

    def __init__(self,name,balance,age):
        bankaccount.count +=1
        self.__acc = bankaccount.count
        self.name = name
        self.balance = balance
        self.age = age 
    def deposite(self,amount):

        return self.balance + amount 
    def withdraw(self,amount):
        if 0 < amount <= self.balance :
            self.balance = self.balance - amount 
        else:
            print(f'insuffucent balance{self.balance}')
    def get_balance(self):
        return self.balance 
    def details(self):
        return self.name , self.age ,self.__acc,self.balance
    
d1 = bankaccount('jay ',20000000,21)
d2 = bankaccount('akash',2000000,19)

d1.deposite(100000)
d2.withdraw(1000)
print(f'detaill1{d1.details()}and {d2.details()}')
              
