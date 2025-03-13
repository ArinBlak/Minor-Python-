import random

lowest = 1
highest = 100
wrong = 0
is_running = True
print("----------------------------Number Guessing Game--------------------------------")
print(f"-----------------------Select a number between {lowest} and {highest}------------------------")

number = random.randint(lowest, highest)

while is_running:
    guess = input("Your guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess > highest or guess < lowest:
            print("Your guess is out of range")
            print(f"Please select a number between {lowest} and {highest}")
        elif guess == number:
            print ("-------------------------------------------------------------------------------")
            print(f"Congrats! You guessed it. It's {number}. You took {wrong} guesses to reach the correct answer")
            break
        elif guess >= number:
            wrong = wrong+1
            print(f"Too High!")
        else:
            wrong = wrong+1
            print(f"Too Low!")
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest} and {highest}")
        