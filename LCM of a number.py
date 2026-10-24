a=int(input("enter a"))
b=int(input("enter b"))
gcd_a,gcd_b=a,b
while gcd_b!=0:
    gcd_a,gcd_b=gcd_b,gcd_a%gcd_b
    gcd=gcd_a
    lcm=(a*b)//gcd
    print(lcm)
