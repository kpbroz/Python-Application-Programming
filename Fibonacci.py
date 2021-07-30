#Generate 'n' Fibonacci sequence 

def fibonacci(n):
    a=0
    b=1
    sum=0
    count=0
    while(count<n):
        print(sum,end=' ')
        a=b
        b=sum
        sum=a+b
        count+=1

n=int(input('Enter a number'))
k=fibonacci(n)
