import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
print(f"The one to pay bill is = {random.choice(friends)}")

# 2nd Option
random_index = random.randint(0, 4)
print(f"The one to pay bill is = {friends[random_index]}")
