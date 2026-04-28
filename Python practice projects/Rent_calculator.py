# Input we need from user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
# Persons living in room/flat

# Output
# Total amount you have to pay is

rent = int(input("Enter your hoste/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (rent + food + total_bill)//persons

print("Each person will pay = ", output)
