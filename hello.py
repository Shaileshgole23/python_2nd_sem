n=10
sum=0
for i in range(1,n+1):
    sum=sum+i
    print(sum)

n=10
sumeven=0
sumodd=0
for i in range(n):
    if i%2==0:
         print(i,"even")
         sumeven+=i
    else:
        print(i,"odd")
        sumodd+=i
print("sum of even numbers",sumeven)
print("sum of odd numbers",sumodd)         





start=int(input("enter start value"))
end=int(input("enter end value"))
for i in range(start,end+1):
    if i%2==0:
         print(i,"even")
         sumeven+=i
    else:
        print(i,"odd")
        sumodd+=i
print("sum of even numbers",sumeven)
print("sum of odd numbers",sumodd)          

#

