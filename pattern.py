#pattern printing
#create a program that prints a pattern of asterisks as shown below:
# *
# **
# ***
# ****


x=int(input("write maximum row"))
for i in range(1,x+1):
    print("*"*i)


#reverse

x=int(input("write maximum row"))
for i in range(x+1,0,-1):
    print(i*"*")
