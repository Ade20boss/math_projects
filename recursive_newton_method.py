def average(x, y):
    return (x+y)/2
def improve(guess, x):
    return average(guess, (x/guess))
def good_enough(guess, x):
    if abs((guess**2) - x) < 0.001:
        return True
    else:
        return False


def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

root = sqrt_iter(1, 2)
print(root)