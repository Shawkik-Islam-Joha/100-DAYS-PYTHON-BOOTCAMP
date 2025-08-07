bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))        # Convert BMI to integer (truncates decimals)
print(round(bmi))      # Round BMI to nearest integer
print(round(bmi, 2))   # Round BMI to 2 decimal places

bmi = round(bmi, 2)

bmi+=1                 # Increase the value by 1

print("Your BMI is = " + str(bmi))

# Printing using fstring is easier

print(f"Your BMI is = {bmi}")