n=int(input("enter a number"))
t=n  
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if t==s:
    print("the number is a palindrome")
else:
    print("the number isn't a palindrome")
