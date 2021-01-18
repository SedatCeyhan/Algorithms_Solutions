def numOfWays(n):
    two_colored, three_colored = 6, 6
    modulo = (10 ** 9) + 7

    for row in range(2, n + 1):
        temp_two_colored = two_colored
        two_colored = (two_colored * 3) + (three_colored * 2)
        three_colored = (temp_two_colored * 2) + (three_colored * 2)

    return (two_colored + three_colored) % modulo

print(numOfWays(5000))
