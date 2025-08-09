import string
import random

# List of lowercase letters
lowercase = list(string.ascii_lowercase)      # ['a', 'b', ..., 'z']

# List of uppercase letters
uppercase = list(string.ascii_uppercase)      # ['A', 'B', ..., 'Z']

# List of digits
nums = list(string.digits)                    # ['0', '1', ..., '9']

# List of special characters (punctuation)
special_characters = list(string.punctuation) # ['!', '"', '#', ..., '~']

print("Hi! Welcome to Password Generator.")

lc = int(input("How many Lowercase characters do you want in your password? : "))
uc = int(input("How many Uppercase characters do you want in your password? : "))
nu = int(input("How many Numbers do you want in your password? : "))
sp = int(input("How many Special characters do you want in your password? : "))
total_length = int(input("Total length of password: "))

if total_length < (lc + uc + nu + sp):
    print("Password Length is invalid for your choice")

password_chars = []

# Add lowercase letters
for i in range(lc):
    password_chars.append(random.choice(lowercase))

# Add uppercase letters
for i in range(uc):
    password_chars.append(random.choice(uppercase))

# Add numbers
for i in range(nu):
    password_chars.append(random.choice(nums))

# Add special characters
for i in range(sp):
    password_chars.append(random.choice(special_characters))

remaining = total_length - (lc + uc + nu + sp)        # If there are remaining characters to fill, pick randomly from all groups
for i in range(remaining):
    password_chars.append(random.choice(lowercase + uppercase + nums + special_characters))

random.shuffle(password_chars)          # Shuffle the resulting list so the order is random

# Convert list into a string . ''.join(list) merges the elements into one continuous string with no separators
password = ''.join(password_chars)

print(f"Your Password is : {password}")


