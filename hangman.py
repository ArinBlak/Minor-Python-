#This is a hangman game and the words for this game are in a seperate list called wordslist

import random

from wordslist import words

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " | ",
                   "   "), 
               3: (" O ",
                   "/| ",
                   "   "),
               4: (" O ",
                   "/|\\",
                   "   "),
               5: (" O ",
                   "/|\\",
                   "/  "),
               6: (" O ",
                   "/|\\",
                   "/ \\")}

def display_art(wrong_guesses):
    print("******************")
    for i in hangman_art[wrong_guesses]:
        print(i)
    print("******************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    wrong_guesses = 0
    guessed_letters = set()
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    is_running = True
    
    while is_running:
        display_art(wrong_guesses)
        display_hint(hint)
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue
        
        if guess in guessed_letters:
            print(f"{guess} has been guessed alresdy")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
        if not "_" in hint:
            display_art(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_art(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE")
            is_running = False

if __name__ == '__main__':
    main()