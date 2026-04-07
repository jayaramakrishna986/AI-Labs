# import random
# # print(random.randint(1,100))
# import numpy as np
# dice = random.randint(56, 65)

# Coin = random.choice(["Head", "Tail"])

# print(dice, Coin)
# print(np.random.randint(0, 5, 2))

# emails = ["spam"]*20 + ["Not_spam"]*80

# p_spam = emails.count("spam")/len(emails)

# print(p_spam)


# file1=open("C:\Users\JayaramakrishnaMedis\OneDrive - Aditi Consulting\Documents\Docs\Notepad-Notes\Git","r")

# with open("C:/Users/JayaramakrishnaMedis/OneDrive - Aditi Consulting/Desktop/File/t1.txt", "w") as file:
#     file.write("Success!")
# with open("C:/Users/JayaramakrishnaMedis/OneDrive - Aditi Consulting/Desktop/File/t1.txt","r+") as file:
#     file.write("I am writing from VS code 121312")
    # print(file.read())
# with open("C:/Users/JayaramakrishnaMedis/OneDrive - Aditi Consulting/Desktop/File/t1.txt","x") as file:
#     file.write("Hello from Agent")
# with open("t1.txt","r") as file:
#     print(file.read())

# try :
#     with open("C:/Users/JayaramakrishnaMedis/OneDrive - Aditi Consulting/Desktop/File/t1.txt","r") as file:
#         content=file.read()
#         print(content)

# except FileNotFoundError:
#     print("Error the file was not found!")

# except PermissionError:
#     print("Permission denied by the user")

# except Exception as e:
#     print("Un expected error")




def myname(namea):
    def getter1():
        print("I am from the before function ")
        namea()
        print("you are from the after function")
    return getter1

@myname
def huii():
    print("sfff")

huii()





# def my_decrator(func):
#     def wrapper():
#         print("Before Function")
#         func()
#         print("After Function")
#     return wrapper

# @my_decrator
# def saY():
#     print("hello")

# saY()


def count_function(n):
    for i in range(n):
        yield i

grn=count_function(6)
for num in grn:
    print(num)




# def genertae_square(n):
#     for i in range(n):
#         yield i*i
# j=genertae_square(5)
# for i in j:
#     print(i)


def hello(g12):
    def wrapper():
        print("Before Function")
        g12()
        print("After Function")

    return wrapper
@hello
def h12():
    print("hello world")

h12()

def sqyare(n):
    for i in range(n):
        yield i*i

l=sqyare(5)
for i in l:
    print(i)