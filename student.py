def Admission():
    Student_ID=input("Enter student Id:-")
    Student_name=input("Enter student name:-")
    Student_age=input("Enter student age:-")
    Student_course=input("Enter student course")
    Student_details={
        'Student ID':Student_ID,
        'Student Name':Student_age,
        'Student Age':Student_age,
        'Student Course':Student_course
    }
    student.append(Student_details)
    print(f"{Student_name} Admit student in university.\n")
def display_Student_details(student):
    if not student:
        print("student not admit")
    