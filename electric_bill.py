# Input electricity unit charges
units = float(input("Enter electricity units consumed: "))

# Initialize variables for the total bill and surcharge
total_bill = 0.0
surcharge = 0.0

# Define the unit-based billing rates and conditions
rate_1 = 0.50  # Rate for the first 50 units
rate_2 = 0.75  # Rate for the next 100 units
rate_3 = 1.20  # Rate for the next 100 units
rate_4 = 1.50  # Rate for units above 250

# Calculate the total bill based on the given conditions
if units <= 50:
    total_bill = units * rate_1
elif units <= 150:
    total_bill = 50 * rate_1 + (units - 50) * rate_2
elif units <= 250:
    total_bill = 50 * rate_1 + 100 * rate_2 + (units - 150) * rate_3
else:
    total_bill = 50 * rate_1 + 100 * rate_2 + 100 * rate_3 + (units - 250) * rate_4

# Calculate the surcharge (20% of the total bill)
surcharge = 0.20 * total_bill

# Add the surcharge to the total bill
total_bill += surcharge

# Display the total electricity bill
print(f"Total Electricity Bill: Rs. {total_bill:.2f}")
