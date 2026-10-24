a=input("enter a string")
v=0
b=0
d=0
s=0
f=0
for i in a:
    if i in "AEIOUaeiou":
        v+=1
    elif i.isalpha():
        b+=1
    elif i.isdigit():
        d+=1
    elif i=="":
        s+=1
    else:
        f+=1
print("vowels: ",v)
print("consonents: ",b)
print("digits: ",d)
print("blankspaces: ",s)
print("othercharacte: ",f)
        
