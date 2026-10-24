#reverse a string without using slicing
s=input("Enter a string:")
r=""
for ch in s:
    r=ch+r    
print("reversed string:",r)
