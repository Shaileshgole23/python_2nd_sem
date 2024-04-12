score=int(input("enter your score"))
if score >= 90:
    grade="A"
elif score >=80:
    grade="B"
elif score >= 70:
    grade="C"
else:
    grade="D"
print("your grade is:" ,grade)