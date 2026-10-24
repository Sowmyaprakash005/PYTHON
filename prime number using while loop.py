n=1
while n<=20:   # OR n>0:
    n+=1
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n,"prime number")
