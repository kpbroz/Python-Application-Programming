#binary equivalent of decimal
k=''
n=int(input('Enter a number'))
while(n!=0):
    m=n%2
    n//=2
    k=k+(str(m))
print(k[::-1])
