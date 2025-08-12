# Tip Calculator 
# Create a tip calculator
print("Welcome to the tip calculator!")
# input the bill amount
bill = float(input("What was the total bill? $"))
# input tip percentage without percentage sign
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# input amount of people splitting the bill 
people = int(input("How many people to split the bill? "))
# calulate amount of total bill 
total_bill = tip/100 * bill + bill
print(total_bill)
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person shoiuld pay: ${final_amount}")


