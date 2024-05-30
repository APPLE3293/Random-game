import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the guessing number game!")
    print("I thought of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Please enter your guess:"))
            attempts += 1

            if guess < number_to_guess:
                print("Too low, try again.")
            elif guess > number_to_guess:
                print("Too high, try again.")
            else:
                print(f"congratulations! You guessed the number correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()