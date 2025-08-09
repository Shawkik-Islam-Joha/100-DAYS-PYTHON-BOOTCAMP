import random
import words_for_hangman

def welcome_text():
    print("Welcome to the Game : HANGMAN")
    print("=============================")

def initialize_word(word):
    return random.choice(word)

def char_check(string,ch):
    if ch in string:
        return string.find(ch)

welcome_text()

mystery_word = initialize_word(words_for_hangman.words)
length = len(mystery_word)
life = 6
your_choice = list("-"*length)

print("".join(your_choice))

while life > 0 and ("-" in your_choice):
    x = input("Enter Your Guess: ")
    idx = char_check(mystery_word,x)
    if idx != None:
        your_choice[idx] = x
        print("".join(your_choice))
    elif idx == None:
        life-=1
        print(f"Wrong Guess! You have {life} chances left")

if ''.join(your_choice) == mystery_word:
    print("You Win!")
elif life == 0:
    print(f"You Lose!\nThe Mystery Word was :{mystery_word}")

