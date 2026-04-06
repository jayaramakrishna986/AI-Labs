# class Student:
#     def __init__(self,name,roll_num,address):
#         self.name =name 
#         self._roll_num=roll_num
#         self._address=address

#     def display(self):
#         print(f"Your name is :{self.name} Roll Num:{self._roll_num} and Address:{self._address}")


# class Teacher(Student):
    
#     def student_details(self):
#         self.display()

#     def roolnum(self):
#         print(self._roll_num)


# class Additon:
#     def add1(self,*args):
#         return sum(args)


    


# s1=Student("Hello",56,"Vadodara")
# s2=Student("Krishna",25,"Vizag")



# # s2.display()

# s3=Teacher("Jiada",34,"adffd")
# s3.student_details()

# s3.roolnum()

# a1=Additon()
# print(a1.add1(1,6,5,2,54,53,1,89))


# class Bank:
#     def __init__(self,account_holder,balance,acct_num):
#         self.account_holder=account_holder
#         self.acct_num=acct_num
#         self._balance=balance

#     def addamount(self,amount):
#         self._balance+=amount
#         print(f"Updated Balance is {self._balance}")
    
#     def display_details_of_person(self):
#         print(f"Account num:{self.acct_num} Account Holder:{self.account_holder} Account Balance:{self._balance}")


#     def changedata(self,new_num=None,new_account_holder=None):
#         if new_num:
#             self.acct_num=new_num
#             print(f"The account number is changed to the {self.acct_num}")
#         if new_account_holder:
#             self.account_holder=new_account_holder
#             print(f"the updated account holder name is {self.account_holder}")

# class Savingsaccount(Bank):
#     def add_interst(self):
#         self._balance=self._balance*0.05
#         print(self.balance)


# b1=Bank("jairam",5000,101)
# b1.display_details_of_person()
# b1.addamount(5000)

# b1.changedata(new_num="123")
# b1.display_details_of_person()

        

# # S1=Savingsaccount("Jairam ")
# # S1.add_interst()

# class Payment:
#     def pay(self):
#         print("Processing payment")


# class UPI(Payment):
#     def pay(self):
#         print("Paying via UPI")


# class Card(Payment):
#     def pay(self):
#         print("Paying via Card")


# for m in [UPI(),Card()]:
#     m.pay()

# from abc import ABC,abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class UPI(Payment):
#     def pay(self,amount):
#         print(f"The amount paid is{amount}")

    
# u1=UPI()
# u1.pay(5656)

class Zomato:
    def __init__(self,Name_of_the_restrant,Location,Phone_num):
        self.Name_of_the_restrant=Name_of_the_restrant
        self.Location=Location
        self.Phone_num=Phone_num
        self.list1=[]
        self.list2=[]
        

    def loaction(self):
        print("A-23,Alembic city,Opposite to inorbit mall,Vadodara,Gujrat")

    def phonenum(self):
        print("Our Phone num:",9010876276)

    def Items(self):
        self.list1=["apple","orange","Graphes","Mango"]
        print(self.list1)

    def Add_Items(self,item1):
        self.list2.append(item1)
        print(self.list2)

    def display_orderd_items(self):
        print(self.list2)

    def isodered(self):
        if len(self.list2)>=1:
            print(f"Yes! You have ordered the items and the items are {self.list2}")

        else:
            print(f"No You are not ordered any of the items you need to add it ")

R1=Zomato("Alekya","Vadodara","9010876")
R1.loaction()
R1.Add_Items("Gulab jam")
R1.Items()
R1.isodered()

class Restaurant:
    
    def __init__(self,name,location,phone):
        self.name=name
        self.location=location 
        self.phone=phone
        self.menu=["Apple","Mango","Grapes","pine apple","Banana"]
        # self.ordereditems=[]
    
    def additem(self,item):
        # self.menu=[]
        self.menu.append(item)

    def show_menu(self):
        print(self.menu)
    @classmethod
    def get_total(cls):
        print(f"total shops are{cls.count}")

class cart:
    def __init__(self):
        self.__items=[]
    
    def add_item(self,item):
        self.__items.append(item)

    def ordereditems(self):
        print(self.__items)

    def is_ordered(self):
        return len(self.__items)>0
    
from abc import ABC,abstractmethod

class Payment:
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self,amount):
        print(f"Amount paid by UPI is :{self.amount}")

class Ordered:
    def __init__(self,cart):
        self.cart=cart

    def place_order(self):
        if self.cart.is_ordered():
            print("Is ordered Sucessfully")

        else:
            print("Cart is Empty")



f1=Restaurant("ABc","Vadodara",1232)
f1.show_menu()
    
f1.additem("sfsfsd")
f1.show_menu()