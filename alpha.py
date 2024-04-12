word=input("enter your value")
alpha=0
digit=0
spec=0
sp=0
for letter in word:
    if letter.isalpha():
        alpha+=1
    elif letter.isdigit():
        digit+=1
    elif letter.isspace():
        sp=sp+1
    else:
        spec+=1
    
print("it is aplphabet ",alpha,"\nit is digit no",digit,"\nit is a space",sp,"\nit is a special chracter",spec)      
    

 