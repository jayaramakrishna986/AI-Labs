
import math
str="Jello"
a=len(str)
print(a)

c="Hello \"owdefw"
print(c)

first ="  Ram"
l1="ROm  "
d1=f"{first}  {l1}"
print(d1.strip())
print(d1)

a1=1
a2=2.43
a3=1+5j
print(type(a1))
print(type(a2))
print(type(a3))

print(round(-1.4))
x=5.9
print(math.ceil(-2.5))
print(math.floor(x))
print(math.tau)



# operators
# +,-,*,/,//,%,**
# print(round(-1.4))//-1
# abs(-1.4)//1.4
# math.ceil(-1.4)//-1
# math.floor(-1.4)//-2
# math.sqrt// for square root of number
# math.cbrt() for cube root of a number


str="apple"
sum=0
for i in range(0,len(str)):
    sum+=ord(str[i])
print(sum)
print("Aag">"BAG") # ascii value of first letter  it is declaring

age=5
message="He is eligible" if age>=18 else "He is not eligible"
print(message)



for i in range(3):
    print("loading"+"."*(i+1))

n=12 #date of completion
msg="You need to review your project" if n<=12 else "you need to complete it soon"
print(msg)


num1 =100
while num1>0:
    print(num1)
    num1=num1//2


num1=6
count=0


for i in range(1,2*num1+1):
    if i%2==0:
        print(i)

        count+=1

print(count)



def greet(name,number):
    print("Hi Your name is", name, "and your number is ",number)

greet("sailu",9010876545)
# print(ada)

file =open(file.txt,"w")

file.write("hello")