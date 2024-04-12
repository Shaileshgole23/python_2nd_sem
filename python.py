#arm strong number checker 
#build a program that checks if a given number is an armstrong number 
#(a number that is equal to the sum of its own digits each raised to the power of the number of digits).
#for example 371 is an armstrong number since 3**3+

num=int(input("Enter number"))
l=len(str(num)) 
total=0
for i in str(num):
    total = total+int(i)**l
if num == total:
    print("yes")
else:
    print("no")