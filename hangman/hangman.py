
def get_words():
    with open("words.txt", "r") as words_file:
        lines = words_file.read().splitlines()
    return lines
import random    

hangman_words = get_words()

secret_word = hangman_words[random.randint(0,852)]
print ("welcome to hangman")
player_name = input("What is your name? ")
print ("hello", player_name)
#print ("the secret word is",secret_word)
number_guesses = 0

while number_guesses < 11:
    player_guess = input ("what's your guess? ")
    guess = player_guess
    for position, letter in enumerate(secret_word):
       if letter == guess: 
           print('HEY YEAH GOT IT at position', position)
       else:
           print('SORRY SUCKER. its not at position', position)
    number_guesses = number_guesses + 1