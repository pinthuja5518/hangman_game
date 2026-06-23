import random

# List of predefined words
words = ["python", "computer", "program", "student", "coding"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Display hidden word
display = ["_"] * len(word)

print("Welcome to Hangman!")

while wrong_guesses < max_wrong and "_" in display:
    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)