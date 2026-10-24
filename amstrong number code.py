n=153
original = n 
s=0
while n>0:
    r=n%10
    s=s+r**3
    n=n//10
if original==s:
    print("amstrong")
else:
    print("not amstrong")
