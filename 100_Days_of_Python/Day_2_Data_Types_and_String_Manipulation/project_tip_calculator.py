print("Welcome to the tip calculator!")

# Get user inputs
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give?\n10, 12, or 15 percent? "))
people = int(input("How many people to split the bill? "))

# Calculate total amount with tip
total_bill = bill + bill * (tip_percent / 100)

# Calculate how much each person should pay
share = total_bill / people

# Display the result upto 2 decimal place
print(f"Each person should pay: ${share:.2f}")          
