# loop 10 times. ask for a letter each time
# and add each letter to a list and print
letters = []
for i in range (10):
    new_letter = input("what's your next letter? ")
    letters.append(new_letter)
    
print(letters)