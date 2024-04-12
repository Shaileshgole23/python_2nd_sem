my_list=["a" ,"b","c"]
my_list.remove("b")
print(my_list)   #rsult #["a", "b"]


my_list1=["a","b","c"]
my_list1.pop(1)
print(my_list1)    #["a","b"]

my_list2=["a","b","c"]
del my_list2[0]
print(my_list2)      #["b","c"] if list already deleted then show error


mylist=["a","b","c"]
mylist.clear()
print(mylist)  # for empty list resul []



mydata=[100,200,300,400,50,60,32]
mydata.sort()
print(mydata)

mydata1=["orange", "mango","kiwi","pineapple","banana"]
mydata1.sort(reverse=True)
print(mydata1)

mydata2=[100,200,50,40,83]
mydata2.sort(reverse=True)
print(mydata2)

mydata3=["banana","orange","kiwi","cherry"]
mydata3.reverse()
print(mydata3)

#a concise way to create lists
squares=[x**2 for x in range(5)]
print(squares)

even_numbers=[x for x in range (10) if x % 2 == 0]
print(even_numbers) # result even number in 1 to 10 #output [0,2,4,6,8]


odd_numbers=[x for x in range (10) if x % 2 != 0]
print(odd_numbers) # result odd number in 1 to 10 # output [1,3,5,7,9]

result=['pass' if score >= 60 else 'Fail' for score in [75,30,85,50]]
print(result)

names=['john','jane','jim']
name_lengths=[len(name) for name in names]
print(name_lengths)


numbers=[x+3 for x in range(1,50) if x%5==0]
print(numbers)

numbers=int(input("write number"))
numbers=numbers+5
for numbers in range(1,50):
    if numbers%5==0:
        print(numbers, end=" # ")
