print("💰 Loan EMI Calculator")

loan_amount = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan period (years): "))

monthly_rate = annual_rate / (12 * 100)
months = years * 12

if monthly_rate == 0:
    emi = loan_amount / months
else:
    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )

total_payment = emi * months
total_interest = total_payment - loan_amount

print("\n----- Loan Details -----")
print("Loan Amount:", round(loan_amount, 2))
print("Interest Rate:", annual_rate, "%")
print("Loan Period:", years, "years")
print("Monthly EMI:", round(emi, 2))
print("Total Payment:", round(total_payment, 2))
print("Total Interest:", round(total_interest, 2))
