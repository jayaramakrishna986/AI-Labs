data=[56,2,54,845,845,5,45,51,2]

# data.append("helloi")
data.insert(2,85)
# data.extend(["adada","wfget"])
print(data.pop())
print(data)
print(data.count(85))

print(data)
data.sort(reverse=True)
print(data)

a=[1,52,96,2]
b=a.copy()
a.append(56)

print(a)
print(b)


asd=[1,2,4,5,6,8]
sqwe=[x *x for x in asd ]
print(sqwe)

cart=[]

cart.extend(["pizza","burger","pizza","cake","burger","cake","burger"])
# cart.remove("pizza")
print(cart)
print(len(cart))
d=[]
for i in cart:
    if i  not in d:
        d.append(i)


print(d)

ms=0
mi=None
for i in cart:
    c=cart.count(i)

    if c>ms:
        ms=c
        mi=i

print(mi)

orders = [
    ["pizza", "burger"],
    ["pizza", "cake"],
    ["burger", "cake"],
    ["pizza", "burger"],
    ["cake"],
    ["pizza","burger"]
]
ti=0
for p in orders:
    ti+=len(p)

print(ti)
# o=[]


# # orders=orders.extend(orders)
# for i in orders:
#     o.extend(i)
# print(o)

# mc=0
# mi=None
# for i in o:
#     c=o.count(i)

#     if mc<c:
#         mc=c
#         mi=i
    
# print(mi)
    
# lc=float('inf')
# li=None

# for i in o:
#     c=o.count(i)
#     if c<lc:
#         lc=c
#         li=i
# print(li)

ci=[]
f_o=orders[0]


        
tuple1=("jairam",56,"India")
name , age , Place=tuple1
print(name,Place)

t1=(1,2,3,2,4,5,2,2,6)

print(t1.count(2))

# users = [
#     ("Jairam", 22),
#     ("Ravi", 25),
#     ("Anu", 21)
# ]
# for u in users:
#     print(u[0])

users = [
    ("Jairam", 22, "Surat"),
    ("Ravi", 25, "Mumbai"),
    ("Anu", 21, "Delhi")
]
avg1=0
sa=0
for i in users:
    sa+=i[1]
c=len(i)
avg1=sa/c
print(sa)


# 2
products = [
    ("Laptop", 50000),
    ("Phone", 20000),
    ("Tablet", 30000)
]
mp=0
for i in products:
    # print(i[0])
    mp+=i[1]
print(mp)

students = [
    ("Jairam", 85),
    ("Ravi", 92),
    ("Anu", 78)
]
ms=0
ms1=[]
for i in students:
    if i[1]>80:
        ms1.append(i[0])
print(ms1)


# Dict

users={
    "Name":"Jairam",
    "Age":56,
    "Place":"Vadodara"
}

print(users["Name"])
print(users.get("Age"))
users["Age"]=89
# print(users)
# users.pop("Age")
# print(users)

for k in users.values():
    print(k )


users.update({"Age":52})

orders = [
    {"item": "pizza", "price": 200},
    {"item": "burger", "price": 150},
    {"item": "pizza", "price": 200}
]
for order in orders:
    # print(order.values())
    for k,v in order.items():
        print(k,v)
# print(i)


