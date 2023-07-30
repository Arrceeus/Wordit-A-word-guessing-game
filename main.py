import random

def word_guessing_game():
    words = ["newyork", "pineapple", "orange", "east", "Mr.Beast"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to the Wordit : A Word Guessing Game!")
    print("Guess the letters of the secret word.Word Guessing Game is a captivating word puzzle game in which players must guess the letters of a secret word within a set number of attempts.")
    print("You have 6 attempts to guess the correct word.")

    while attempts > 0:
        print("\nYour Word:", end=" ")
        for letter in secret_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        if set(secret_word) == set(guessed_letters):
            print("\nCongratulations! You guessed the word correctly!")
            break

        print("\nAttempts Remaining:", attempts)
        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                attempts -= 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

    if attempts == 0:
        print("\nGame Over! You ran out of attempts.")
        print("The secret word was:", secret_word)

word_guessing_game()
