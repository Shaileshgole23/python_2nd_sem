val=input("enter value")
digit=""
alphabets=""
for i in val:
    if i.isalpha():
        alphabets+=i
    elif i.isdigit():
        digit+=i
print("alphabets are=",alphabets,"\ndigit are=",digit)
        
