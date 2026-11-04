# Simple calculater 
num1=int(input("enter a number 1:"))
num2=int(input("enter a number 2:"))
op=input("enter a operater(=,-,*,/):")
if op=="+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op =="*":
    print(num1*num2)
elif op =="/":
    if num2!=0:
        print(num1/num2)
    else:
        print("cannot divide by zero")
elif op =="%":
    if num2!=0:
        print(num1%num2)
    else:
        print("cannot divide by zero")
