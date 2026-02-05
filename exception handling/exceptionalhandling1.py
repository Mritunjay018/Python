#valid age for work 
class invalidageerror(Exception):
    pass


def validiation_age(age):
    if age>=18 and age <60:
        return True
    else:
        raise invalidageerror("age should be between 18 to 60")
    

name = input("Enter your name")
age = int(input("enter your age"))

try:
    validiation_age(age)
    print('you can join work')
except invalidageerror as e:
    print(e)











    




