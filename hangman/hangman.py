
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
print ("Number of letters in the secret word is",len(secret_word))
number_guesses = 0
progress = []
for i in range(len(secret_word)):
    progress.append('_')
    
while number_guesses < 11:
    print("Word is", progress)
    player_guess = input ("what's your guess? ")
    guess = player_guess
    for position, letter in enumerate(secret_word):
       if letter == guess:
           progress[position] = guess
    number_guesses = number_guesses + 1
    if '_' in progress:
        print("Sorry you're done")
    else:
        print ("Great job, you finished!")
        break
    