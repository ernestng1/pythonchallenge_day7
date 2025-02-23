import random
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = []
for i in chosen_word:
    placeholder.append("_")

print("".join(placeholder))

game_over = False
counter = 0
position = 0
lives = 6

while game_over == False:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in placeholder:
        print(f"You have already guessed the letter {guess} it before!")
    else:
        if guess in chosen_word:
            for letter in chosen_word:
                if letter == guess:
                    placeholder[position] = guess
                    counter += 1
                position +=1
            print(stages[lives])
        else:
            lives -= 1
            print(stages[lives])
            print(f"{guess} is not the correct word")

    if lives == 0:
        game_over = True
        print("***********************YOU LOSE**********************")
    elif counter == len(chosen_word):
        game_over = True
        print("***********************YOU WIN**********************")

    position = 0
    print("".join(placeholder))


