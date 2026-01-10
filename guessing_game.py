
import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Welcome to the Guessing Game!")
print(f"select a number between {lowest_num} and {highest_num}.")

while is_running:
    guess = input("make a guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"please select a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print("too low. try again.")
        elif guess > answer:
            print("too high. try again.")
        else:
            print(f"congratulations! you guessed the number {answer} in {guesses} attempts.")
            is_running = False

else:
    print("invalid guess. please enter a number.")
    print(f"select a number between {lowest_num} and {highest_num}.")
