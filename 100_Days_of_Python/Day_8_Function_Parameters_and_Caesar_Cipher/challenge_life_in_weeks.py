def life_in_weeks(age):
    age = 90 - age
    age*=52
    return age

x = int(input("Enter Your Age: "))

print(f"You have {life_in_weeks(x)} weeks left!")