print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_bill = 0
vat = 7

# todo: work out how much they need to pay based on their size choice.

if size == 'S':
    total_bill += 15
elif size == 'M':
    total_bill += 20
else:
    total_bill += 25

# todo: work out how much to add to their bill based on their pepperoni choice.

if pepperoni == 'Y':
    total_bill += 3

# todo: work out their final amount based on whether if they want extra cheese.

if extra_cheese == 'Y':
    total_bill += 1

# todo: work out their final amount including VAT

total_bill += total_bill*(vat/100)          

print(f"Your Total Payable : ${total_bill:.2f}")
