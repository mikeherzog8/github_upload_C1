# coding: utf-8
import csv
from pathlib import Path 

#"""Part 1: Automate the Calculations.

#Automate the calculations for the loan portfolio summaries.

loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
print(number_of_loans)

total_of_loans = sum(loan_costs)
print(total_of_loans)

average_loan_amount = total_of_loans / number_of_loans
print(average_loan_amount)

#"""Part 2: Analyze Loan Data.

#Analyze the loan to determine the investment evaluation.

#"""


# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

print(loan.get('future_value'))
print(loan.get('remaining_months'))

loan_price = loan.get('loan_price')
future_value = loan.get('future_value')
remaining_months = loan.get('remaining_months')
discount_rate = 0.2

present_value = future_value/(1+discount_rate/12)**remaining_months
print(f"Present Value is ${present_value: .2f}")

if present_value > loan_price:
    print("Yes! This loan is worth it!")
else: 
    print("Pass on this loan! Too Expensive!")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

loan_price = loan.get('loan_price')
future_value = loan.get('future_value')
remaining_months = loan.get('remaining_months')
discount_rate = 0.2

present_value = future_value/(1+discount_rate/12)**remaining_months
print(f"Present Value is ${present_value: .2f}")

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate/ 12)) ** remaining_months
    return present_value

annual_discount_rate = 0.20
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)

print(f"The present value of the loan is: ${present_value: .2f}")   




#"""Part 4: Conditionally filter lists of loans.

#In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

#1. Create a new, empty list called `inexpensive_loans`.
#2. Use a for loop to select each loan from a list of loans.
   # a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
   # b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
#3. Print the list of inexpensive_loans.
#"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan_price in loans:
    if loan_price["loan_price"] <= 500:
        inexpensive_loans.append(loan_price)



# @TODO: Print the `inexpensive_loans` list
print(inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
