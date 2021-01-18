def isHappy(n):
    unique_squares = set()
    while n != 1 and n not in unique_squares:
        unique_squares.add(n)
        total = 0
        for i in range(len(str(n))):
            total += int(str(n)[i]) ** 2
        n = total

    return n == 1



