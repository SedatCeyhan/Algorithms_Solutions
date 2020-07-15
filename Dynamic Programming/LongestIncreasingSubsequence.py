def lengthOfLIS(nums):
    n = len(nums)
    if n == 0: return 0

    dp = [0] * (n + 1)

    max_length1 = 0
    for i in range(1, n + 1):
        max_length2 = 0
        for j in range(1, i):
            if nums[j - 1] < nums[i - 1] and max_length2 < dp[j]:
                max_length2 = dp[j]

        dp[i] = max_length2 + 1
        if max_length1 < dp[i]: max_length1 = dp[i]

    return max_length1


print(lengthOfLIS([]))


# Python 3 implementation to find the length of
# longest increasing contiguous subarray


# function to find the length of longest
# increasing contiguous subarray
def lenOfLongIncSubArr(arr, n):
    # 'max' to store the length of longest
    # increasing subarray
    # 'len' to store the lengths of longest
    # increasing subarray at diiferent
    # instants of time
    m = 1
    l = 1

    # traverse the array from the 2nd element
    for i in range(1, n):

        # if current element if greater than previous
        # element, then this element helps in building
        # up the previous increasing subarray encountered
        # so far
        if (arr[i] > arr[i - 1]):
            l = l + 1
        else:

            # check if 'max' length is less than the length
            # of the current increasing subarray. If true,
            # then update 'max'
            if (m < l):
                m = l

            # reset 'len' to 1 as from this element
            # again the length of the new increasing
            # subarray is being calculated
            l = 1

    # comparing the length of the last
    # increasing subarray with 'max'
    if (m < l):
        m = l

    # required maximum length
    return m


# Driver program to test above

arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]
n = len(arr)
print("Length = ", lenOfLongIncSubArr(arr, n))

# This code is contributed
# by Nikita Tiwari.












































