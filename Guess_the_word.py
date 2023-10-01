import random

# List of words to scramble
word_list = ["python", "programming", "computer", "keyboard", "monitor", "mouse", "algorithm", "variable","coding","blockchain","analysis","class","encapsulation"]

# Function to select a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to scramble a word
def scramble_word(word):
    word_chars = list(word)
    random.shuffle(word_chars)
    return ''.join(word_chars)

# Function to play the game
def play_game():
    score = 0

    print("Welcome to the Word Scramble Game!")
    print("Unscramble the word to earn points. Type 'quit' to exit.")

    while True:
        selected_word = choose_word()
        scrambled_word = scramble_word(selected_word)

        print(f"Scrambled word: {scrambled_word}")
        guess = input("Your guess: ").lower()

        if guess == 'quit':
            break

        if guess == selected_word:
            score += 1
            print(f"Correct! Your score: {score}")
        else:
            print("Incorrect. Try again!")

    print(f"Your final score: {score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
