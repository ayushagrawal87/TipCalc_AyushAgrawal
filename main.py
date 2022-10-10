print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill? \n₹"))
tip = int(input("What percent tip would you like to give? 10%, 12% or 15% (Enter only number in answer. Ex: 10)?\n"))
people = int(input("How many people to split the bill?\n"))
tip_multiplier = 1 + (tip/100)
net_bill = tip_multiplier * total_bill
tip_per_person = round(net_bill / people)
print(f"The net bill would be  + ₹{net_bill}")
print(f"Each person should pay {tip_per_person} approx.")
