def reverseAndAdd(num):
    count = 0
    maxLength = 4294967295
    while count < 1000:
        num += int(str(num)[::-1])
        if isPalindrome(str(num)) and num <= maxLength:
            return num
        count += 1

    return "No Palindrome Exists!"


def isPalindrome(num):
    if not num: return True
    return num[0] == num[-1] and isPalindrome(num[1:-1])




print(reverseAndAdd(196))
