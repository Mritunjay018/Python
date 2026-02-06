#bank withdrwal 
class insufficientfunderror(Exception):
    pass

def withdraw(balance,amount):

    if amount>balance:
     raise insufficientfunderror("not enough")
    return balance - amount

balance = 5000
amount = int(input(":enter amount"))

try:
   
   balance =withdraw(balance,amount)
   print("withdrwal succesful")
   print("remaining balance",balance)
except insufficientfunderror as e:
   print(e)








