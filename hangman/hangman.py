
def get_words():
    with open("words.txt", "r") as words_file:
        lines = words_file.read().splitlines()
    
    return lines
    
hangman_words = get_words()