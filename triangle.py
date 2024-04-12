# Input the lengths of the three sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the triangle is valid
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")


