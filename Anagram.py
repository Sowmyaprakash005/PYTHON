s1=input("enter a string 1")
s2=input("enter a string 2")
s1=s1.lower()
s2=s2.lower()
s1=s1.replace(" ","")
s2=s2.replace(" ","")
if sorted(s1)== sorted(s2):
    print("it is an anagram")
else:
    print("not an anagram")
