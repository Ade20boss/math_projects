def square_root(number):
    guess = 0
    new_guess = 0
    if number == 0:
        print(0)
        return
    if number >= 1:
        guess = number / 2
    elif 0 < number < 1:
        guess = 1
    while True:
        new_guess = (guess + (number/guess))/2
        if abs((new_guess**2)-number) < 0.1:
            print(new_guess)
            break
        guess = new_guess



square_root(2)