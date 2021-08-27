#program to count the numbers, alphabets and special characters in a given string 
n=0
a=0
s=0
c=input('Enter a string ')
for i in c:
    if ord(i)>=48 and ord(i)<=57:
        n+=1
    elif ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
        a+=1 
    else:
        s+=1
print('numbers=',n,'\nalbhabets=',a,'\nspecial characters=',s)
