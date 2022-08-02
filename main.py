import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
already_guessed = []

from hangman_art import logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()  

    
  
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess in already_guessed:
      if guess not in display:
        lives += 1
      print(f"You have already guessed '{guess}'")

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word\n")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The correct answer was '{chosen_word}'")
        

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    already_guessed += guess

    from hangman_art import stages
    print(stages[lives])

    

    