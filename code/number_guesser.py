print("Please pick a whole number between 1 - 100: ")
game_on = True
a = 1
b = 100
# a = previous number that got the 'larger' response
# b = previous number that got the 'smaller' response
# we can say to pick a number between those two
def bisection_algorithm(a,b):
    return (a + b) // 2

while game_on == True:
    guess_num = bisection_algorithm(a,b)
    print("My guess is ", guess_num, ": ")
    response = input("Is my guess correct, too high, or too low? ")
    if response == "Too high" or response == "too high" or response == "Too High":
        b = guess_num
    if response == "Too low" or response == "too low" or response == "Too Low":
        a = guess_num
    if response == "Correct" or response == "correct":
        print("Yay! Thanks for playing :) ")
        game_on = False