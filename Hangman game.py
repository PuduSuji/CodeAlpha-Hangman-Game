import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "strawberry", "watermelon","custurd apple","papaya","kiwi","pear"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while incorrect_guesses < max_attempts:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1
            print("Attempts remaining:", max_attempts - incorrect_guesses)

    else:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
