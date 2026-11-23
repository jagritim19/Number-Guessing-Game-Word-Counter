import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    score = 100

    print("\n=== NUMBER GUESSING GAME ===")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Your guess must be between 1 and 100.")
            continue

        attempts += 1

        if guess == secret_number:
            earned_score = max(10, score - (attempts - 1) * 10)
            print(f"Correct! You guessed the number in {attempts} valid attempt(s).")
            print(f"Your score: {earned_score}/100")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    else:
        print(f"\nGame over! The correct number was {secret_number}.")
        print("Your score: 0/100")

    again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if again in ("yes", "y"):
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
