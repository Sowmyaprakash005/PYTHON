w=input("enter a word:")
freq={}  
for ch in w:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print("frequencies:")
for ch,cnt in freq.items():
    print(ch," ",cnt)
