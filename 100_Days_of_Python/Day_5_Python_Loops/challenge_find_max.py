import random

scores = []
scores.extend([random.randint(1,100) for i in range(100)])

max_score = 0

for x in scores:
    if x > max_score:
        max_score = x

print(max_score)
