def get_words():
    with open("words.txt", "r") as words_file:
        lines = words_file.read().splitlines()
    return lines
import random    

hangman_words = get_words()

secret_word = hangman_words[random.randint(0,852)]
secret_word = secret_word.lower()
wrong_letters = []
print ("welcome to hangman")
player_name = input("What is your name? ")
print ("hello", player_name)
print ("Number of letters in the secret word is",len(secret_word))

"""
for i in range (10):
    new_letter = input("what's your next letter? ")
    letters.append(new_letter)
    
print(letters)
"""

number_guesses = 0
progress = []
for i in range(len(secret_word)):
    progress.append('_')
    
while number_guesses < 9:
    print("")
    print("Word is", progress)
    print("you have guessed",wrong_letters)
    player_guess = input ("what's your guess? ")
    guess = player_guess
    
    letter_in_word = False
    for position, letter in enumerate(secret_word):
       if letter == guess:
           letter_in_word = True
           progress[position] = guess
    
    if letter_in_word is False:
        wrong_letters.append(guess)
        number_guesses = number_guesses + 1
    if '_' in progress:
        print("Sorry not done, you have used", number_guesses, "guesses")
    else:
        print ("Great job, you finished!")
        break
    