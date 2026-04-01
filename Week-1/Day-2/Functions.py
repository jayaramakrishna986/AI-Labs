def greet():
    print("Hello How are you?")

greet()
          


def addtion(a,b):
    return a+b
a1=addtion(3,4)
print(a1)

def squafreofn(n):
    return n*n

print(squafreofn(7))

n1=lambda  y:y+2

print(n1(89))

def sum1(*nums):
    return sum(nums)

# print(sum1(1,3,34,4))
a1=sum1(1,3,4,5)
print(a1)


# recurssion 
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

a1=fact(4)
print(a1)

# reverse a String

a="hell"
a=list(a)
l=0
r=len(a)-1
while l<=r:
    a[l],a[r]=a[r],a[l]
    l+=1
    r-=1

a="".join(a)

print(a)

#plaindrome
a=121121
a=str(a)
s=a
if a==a[::-1]:
    print("Yes")
else:
    print("No")


num=112212121
d1=num
rem=0
    
while num>0 :
    d=num%10
    rem=rem*10+d
    num=num//10
    
# print(rem)
if rem == d1:
    print("Yes!!!")
else:
    print("No!!!")


def palindorome(n):
    s=n
    rem=0
    while n>0:
        d=n%10
        rem=rem*10+d
        n//=10
    
    if rem == s:
        print("Yes it is and palindrome Number!!")
    else:
        print("No it is not a palindrome number")

palindorome(2332)


# reverse a string with out slicing

def reverse(str):
    result=""
    for i in str:
        result=i+result
    return result


print(reverse("Hello"))