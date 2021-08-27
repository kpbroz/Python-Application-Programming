i=0
sum=0
while True:
    n=input('Enter a number')
    if n is 'done':
        break
    try:
        n=float(n)
        i+=1
        sum+=n
    except:
        print('bad input')
avg=sum/i
print('sum',sum)
print('avg',avg)
