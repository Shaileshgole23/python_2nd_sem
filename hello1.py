#write a program to print the multification table of a given number up to a specified range(e.g,10)
num=int(input("write a positive number"))
for i in range(1,11):
    if num<=0:
        print("invalid")
    else:
        print(num,"*",i,"=",num*i)

#factorial
#create a program that calculates the factorial of a given number
#the factorial of a number is the multification of all the numbers between 1 and the number it self

num=int(input("enter your number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"the factorial of {num} is:",{fact})

#fibonacci sequence
#problem: write a program that generates the fibonacci sequence up to a specified limit(e.g.,less than 1000).
#the sequence follows the rule that each number is equal to the sum of the preceding two numbers. the fibonacci sequence begins with the
#following 14 integers: 0,1,2,3



limit=int(input("enter the number"))
num1=0
num2=1
num3=0
print(num1)
for num in range(1,limit+1):
    num1=num2
    num2=num3
    num3=num1+num2
    print(num3)
      


