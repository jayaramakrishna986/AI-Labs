# OOps Object oriented programming

# class ->blue print of an object
# Object ->Real world instance

from abc import ABC,abstractmethod
class Student:
    def   __init__(self,name,number1):
        self.name =name 
        self.number1=number1
        print("The details are filled your own")
    
    def display_details(self):
        print("Your name is",self.name,"your number is",self.number1)


c1=Student("Jairam",910012323435)
c1.display_details()



class Car:
    car_name = "BMW"

    def __init__(self,model,milage,seater):
        self.model=model
        self.milage=milage
        self.seater=seater
    @classmethod
    def carnamechange(self,namech):
        self.namech=namech

    @staticmethod
    def isvalid(seater):  
        return seater<6

    def display(self):
        print(self.model ,self.milage,self.seater,self.car_name) 

    
c2=Car(2.1,18,3)
c2.carnamechange("Audi")
c2.display()
print(c2.isvalid(5))


class Office:
    office_type="Private"
    def __init__(self,name,address,date):
        self.name=name
        self.address=address
        self.date=date

    def display(self):
        print("Office name:",self.name,"   Office Address:",self.address,"   Date of Join",self.date,self.office_type)


    @classmethod
    def changeofofficetye(self,name1):
        self.office_type=name1

    @staticmethod
    def isverified(date)  :
        return 1<date<30

o1=Office("Aditi","Vadodara",30)
o1.changeofofficetye("Protected")
o1.display()
# print(o1.isverified)
print(o1.isverified(54))



#Encapsulation

class Bankaccount:
    def __init__(self,balance):
        self.__balance=balance

    def depoist(self,amount):
        self.__balance+=amount

    def get_balance(self):
        print("Your amount is",self.__balance)
        # return self.__balance
u1=Bankaccount(5000)
u1.depoist(2000)
u1.get_balance()


#Abstarction

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class Cerditcard(Payment):
    def pay(self,amount):
        print("Paid using the Cerdit card:",amount)

class UPI(Payment):
    def pay(self,amount):
        print("Paid using the UPI",amount)

p1=Cerditcard()
p1.pay(5000)
p2=UPI()
p2.pay(6000)


#inheritance

class A:
    def action(self):
        print("I will swim in the water")
    
class B(A):
    def Movement(self):
        print("I will Walk faster then you")

a12=A()
a12.action()
a113=B()
a113.Movement()
a113.action()#we can access the upper class from the child class


class A:
    def pass1(self):
        print('hello from pass1')

class B:
    def pass2(self):
        print('hello from pass2')
    
class C(A,B):
    pass

c1=C()
c1.pass1()


# Polymorpsim
#method overriding
class Animal:
    def sound(self):
        print("I used to sound during night")

class Dog:
    def sound(self):
        print("I used to Bow bow")

class Cat:
    def sound(self):
        print("I used to sound meow meow")

c1=Cat()
d1=Dog()

c1.sound()
d1.sound()

#method overloading

# class Maths:
class Maths:
    def add1(self,a,b):
        return a+b
    
    def add1(self,a,b,c=0):
        return a+b+c
    
m1=Maths()
print(m1.add1(1,2))
print(m1.add1(4,5,6))