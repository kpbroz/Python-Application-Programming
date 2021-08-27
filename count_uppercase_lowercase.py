#Program to print the count of letters, digits, lowercase , uppercase in a string

d={'LETTERS':0,'DIGITS':0,'LOWERCASE':0,'UPPERCASE':0}
s=input('Enter a string\n')

for i in s:
    if ord(i) in range(65,91):
        d['UPPERCASE']+=1
    elif ord(i) in range(97,123):
        d['LOWERCASE']+=1
    elif ord(i) in range(48,58):
        d['DIGITS']+=1
d['LETTERS']=d['UPPERCASE']+d['LOWERCASE']
print(d)
