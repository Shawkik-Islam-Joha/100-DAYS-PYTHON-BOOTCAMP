# ––•–√\/––√\/––•––

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        bill += 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 60:
        bill += 0
        print("Oldies tickets are free!")
    else:
        bill += 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.\n")
    if wants_photo == "y":
        bill += 3                           # Add $3 to their bill
   
    bill += bill * (5 / 100)

    print(f"Your final bill is ${bill:.2f}")
else:
    print("Sorry you have to grow taller before you can ride.")
