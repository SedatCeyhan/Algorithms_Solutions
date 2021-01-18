# Python3 program for the above approach

# Function to return minimum distinct
# character after M removals
def distinctNumbers(arr, m):
    n = len(arr)
    if n == 0: return 0
    count = {}

    # Count the occurences of number
    # and store in count
    for i in range(n):
        count[arr[i]] = count.get(arr[i], 0) + 1

    # Count the occurences of the
    # frequencies
    fre_arr = [0] * (n + 1)
    for it in count:
        fre_arr[count[it]] += 1

    # Take answer as total unique numbers
    # and remove the frequency and
    # subtract the answer
    ans = len(count)

    for i in range(1, n + 1):
        temp = fre_arr[i]
        if (temp == 0):
            continue

        # Remove the minimum number
        # of times
        t = min(temp, m // i)
        ans -= t
        m -= i * t

        # Return the answer
    return ans


# Driver Code
if __name__ == '__main__':
    # Initialize array
    #arr = [2, 4, 1, 5, 3, 5, 1, 3]
    arr = [1,1,1,2,3,2]

    # Size of array
    m = 2

    # Function call
    print(distinctNumbers(arr, m))

    # This code is contributed by mohit kumar 29