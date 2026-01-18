import random

options = ("rock", "paper", "scissors")
is_running = True

while is_running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("rock, paper, or scissors? : ").lower()
        
        if player not in options:
            print("Invalid option! Please enter rock, paper, or scissors.")

    print(f"computer: {computer}")
    print(f"player: {player}")

    if player == computer:
        print("it's a tie!")
    elif (player == "rock" and computer == "scissors"):
        print("you win!")
    elif (player == "paper" and computer == "rock"):
        print("you win!")
    elif (player == "scissors" and computer == "paper"):
        print("you win!")
    else:
        print("you lose!")
    
    if not input("play again? (yes/no): ").lower() == "y":
        is_running = False

print("*******************")
print("thanks for playing!")
print("*******************")