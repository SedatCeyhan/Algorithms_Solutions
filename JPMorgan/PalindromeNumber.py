def isPalindrome(x):

    def isPalindromeString(s):
        if not s: return True
        return s[0] == s[-1] and isPalindromeString(s[1:-1])

    if not x: return True
    if str(x)[0] == "-": return False
    return isPalindromeString(str(x))

print(isPalindrome(88))