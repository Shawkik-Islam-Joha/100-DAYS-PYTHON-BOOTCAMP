import random
import words_for_hangman                # To access the list 'words' from words_for_hangman.py

print("Welcome to the Game : HANGMAN")
print("=============================")

x = int(input("Enter 1 to start, Enter 0 to end.\n"))

if x == 0:
    exit()

the_mystery_word = random.choice(words_for_hangman.words)
length = len(the_mystery_word)
life = 6
your_guess = list("_"*length)

print("".join(your_guess))

while ("_" in your_guess) and life > 0:
    ch = input("Enter Your Guess: ")
    idx = the_mystery_word.find(ch)
    if idx != -1:
        your_guess[idx] = ch
    else:
        life-=1
        print(f"Wrong Guess! Chance left : {life}")
    print("".join(your_guess))              # Convert the list to string to print

if "".join(your_guess) == the_mystery_word:
    print("Congratulations!\nYou win!")
elif life == 0:
    print("You Lose!")


