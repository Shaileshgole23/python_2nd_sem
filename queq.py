#problem statement
#write a funtion that takes a list of numbers as an argument
#and returns the sum of the squares of those numbers.
list=[]
num=int(input("enter the number:"))
for i in range(1,num+1):
    list_item=int(input(f"enter the list item{i}:"))
    list.append(list_item)
print(list)
def sum_of_squares(x):
    sum_of_squares=0
    for i in x:
        sum_of_squares+=i**2
    print("sum of squares",sum_of_squares)
sum_of_squares(list)

