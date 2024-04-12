# my_student={
#     "stud1":{
#         "name" : "sachin+",
#         "year": 2004
#     },
#     "stud2":{
#         "name":"Laxman",
#         "year": 2007
#     },
#     "stud3":{
#         "name": "ram",
#         "year": 2011
#     }
# }
# print(my_student)
# for x in my_student:
#     print(x)
# print(my_student["stud2"]["name"])
# for x,y in my_student.items():
#     print(x,y)

# # you are required to create a python program that allows a user to input key value pairs
# #to construct a dictionary . the program should follow these steps:
# # 1. prompt the user to enter the number of key-value pairs they want to add.
# #2 for each pair , prompt the user to enter a key and its corresponding value.
# #3 construct a dictionary with the provided key-value pairs.
# #4 print out the resulting dictionary. 
# user_dict={}
# num=int(input("enter number of key value pairs you want to"))
# for x in range(num):
#     key= input("enter the key:")
#     value= input("enter the value:")
#     user_dict[key]=value

#     print("resulting dictionary")
#     print(user_dict)

#creating and manipilation dsictionary 

# dic={"jonh": 85, "jane":90,"bob":75,"alice":95}
# dic["sam"]=80
# dic["bob"]=80
# del dic["jane"]
# for name_score in dic.items():
#     print(f"(name):(score)")

grades={"jonh": 85, "jane":90,"bob":75,"alice":95}
highest_grade= -1
for grade in grades.values():
    if grade > highest_grade:
        highest_grade=grade
top_students=[student for student, grade in grades.items() if grade == highest_grade]
print(f"the highest grade is:(highest_grade)")
print(f"the student(s) with the highest grade:{','.join(top_students)}")