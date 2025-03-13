import random

print("Lets play rock, papers and scissors")
options = ("rock", "paper", "scissor")
running = True

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter your choice (rock, paper or scissor): ")
    
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    
    if player == "rock" and computer == "scissor":
        print("You win")
    elif player == "scissor" and computer == "paper":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == computer:
        print("It's a tie")
    else:
        print("I win")
    
    if not input("Want to play again? (y/n)").lower() == "y":
        running = False