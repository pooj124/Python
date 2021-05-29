import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_over = False
lives = len(stages) - 1

randomly_chosen_word = random.choice(word_list)
word_length = len(randomly_chosen_word)

# displaying "_" for the length of the randomly_selected_word
display = []
for _ in range(word_length):
    display += "_"

while not game_is_over:
    guess = input("Guess a letter : ").lower()
    clear()  # to clear outputs between guesses

    if guess in display:
        print(f"You've already guessed {guess}")

    # showing the user that their guess was right
    for pos in range(word_length):
        letter = randomly_chosen_word[position]
        if letter == guess:
            display[postion] = letter
            print(f"{' '.join(display)}")

        # Make the player loose a live if they guess is wrong
        # "not" can be used for negation
    for guess not in randomly_chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

if lives == 0:
    game_is_finished = True
    print(f"You lose.\n\nThe word was '{randomly_chosen_word}'.")

# Looking to see if all the blanks are filled in
if not "_" in display:
    game_is_finished = True
    print("You win.")

print(stages[lives])
