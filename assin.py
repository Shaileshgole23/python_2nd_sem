def calculate_monthly_payment(principal, annual_interest_rate, loan_term_years):
    
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_payments = loan_term_years * 12
    
    
    monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate)**total_payments) / \
                      ((1 + monthly_interest_rate)**total_payments - 1)
    
    return monthly_payment


principal = float(input("Enter the principal amount of the loan: "))
annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
loan_term_years = float(input("Enter the loan term in years: "))


monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, loan_term_years)
print(f"The monthly payment for the education loan is: ${monthly_payment:.2f}")
