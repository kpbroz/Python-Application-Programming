#fibonacci series using recursion

def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
num=10
for i in range(num):
    print(fibo(i))
