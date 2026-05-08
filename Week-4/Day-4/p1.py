import time
def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
start=time.time()
fib(56)
print(time.time()-start)
