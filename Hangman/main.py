import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

chosen_word = random.choice(word_list)
word_len = len(chosen_word)

end_of_game = False
lives = 6
print(logo)

display = []
for i in range(word_len):
    display += '_'

while not end_of_game:

    guess = input("Guess a letter:").lower()
    if guess in display:
        print(f"you've already guessed {guess}")

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"you've guessed {guess} that's not in word . You lose!")
        lives -= 1
        if lives == 0:
            end_of_game=True
            print('you lose!')

    print(f"{''.join(display)}")
    if "_" not in display:
            end_of_game=True
            print('you win')
        
    print(stages[lives])
        

    
