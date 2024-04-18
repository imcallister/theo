
game_on = True
def is_factor(k, n):
    input_1 = int(n)
    input_2 = int(k)
    if input_1 % input_2 == 0:
        return True
    else:
        return False

def is_prime(n):

    for i in range(2,n):
        if is_factor(i, n) == False:
            pass
        else:
            return False
    return True

while game_on == True:
    input_ = (input('Please enter a positive integer:  '))
    if input_ == "q":
        game_on = False
    else:
        input_num = int(input_)
        if input_num < 2:
            print("is neither")
        else:
            if (is_prime(input_num)) == True:
                print("is prime")
            else:
                print("is composite")