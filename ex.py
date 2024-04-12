#for identidy chracters
num=input("enter your character")
if num.isalpha():
    print(f"'{num}' is an alphabet")
elif num.isdigit():
    print(f"'{num}' is a digit ")
else:
    print(f"'{num}' is a special character")

#basic salary of the employee

# Input the basic salary of the employee
basic_salary = int(input("Enter the basic salary: "))

# Constants for allowances (as percentages of the basic salary)
hra_percentage = 0.0  # Initialize HRA percentage
da_percentage = 0.0  # Initialize DA percentage

# Determine HRA and DA percentages based on the basic salary
if basic_salary <= 10000:
    hra_percentage = 0.20  # 20% of basic salary
    da_percentage = 0.80  # 80% of basic salary
elif basic_salary <= 20000:
    hra_percentage = 0.25  # 25% of basic salary
    da_percentage = 0.90  # 90% of basic salary
else:
    hra_percentage = 0.30  # 30% of basic salary
    da_percentage = 0.95  # 95% of basic salary

# calculate hra and da with the help of given data 
hra = basic_salary * hra_percentage
da = basic_salary * da_percentage

# Calculate the gross salary
gross_salary = basic_salary + hra + da

# Display the components and gross salary
print(f"Basic Salary: {basic_salary:.2f}")
print(f"HRA: {hra:.2f}")
print(f"DA: {da:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")


