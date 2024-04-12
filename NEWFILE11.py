#Reverse a number 
#write a program that reverses a give number (eg 12345 becomes 54321)
num=int(input("enter your number" ))
reversed_number=0
while num>0:
    digit=num%10
    reversed_number=(reversed_number*10)+digit
    num=num//10
print(f"The reversed number is:{reversed_number}")  
