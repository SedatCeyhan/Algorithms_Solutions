import math

def getMoneyAmount(n):
    guess = int(math.ceil(n/2))
    sum = 0

    while guess != n:
        sum += guess
        guess = int(math.ceil((n + guess)/2))

    return sum

print(getMoneyAmount(1))
