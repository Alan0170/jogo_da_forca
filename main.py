import random
from jogo_da_forca_figuras import stages, logo
from jogo_da_forca_palavras import word_list
import os

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Advinhe uma letra ").lower()

    os.system('cls')

    if guess in display:
        print(f"Você já advinhou! {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print("Boa! Essa letra está na palavra")
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"Você disse {guess}, essa letra não está na palavra. Você perdeu uma vida!")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("Você Perdeu!")
    
    if not "_" in display:
        game_is_finished = True
        print("Você ganhou!")

    print(stages[lives])