def longest_flat(array):
    # If array is empty, then there is no continuous stretch: return 0
    if len(array) == 0: return 0

    # Dynamic Programming: Create a list of length n, where each
    # item in the array has a value = 1. This is bc all numbers are trivially stretches of themselves.
    n = len(array)
    dp = [1] * (n)

    # Since array isn't empty, initially the longest stretch is >= 1
    longest = 1

    # Find the longest stretch
    for i in range(1, n):
        if array[i] == array[i - 1]:
            dp[i] = 1 + dp[i - 1]
            if longest < dp[i]:
                longest = dp[i]

    return longest


print(longest_flat([1,2,3,4,5,6,5,7,5,5]))

