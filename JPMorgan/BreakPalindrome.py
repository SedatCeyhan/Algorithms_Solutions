def breakPalindrome(palindrome):
    if not palindrome or len(palindrome) == 1: return ""
    for i in range(len(palindrome)):
        if palindrome[i] != 'a':
            if i != len(palindrome) - 1 - i: return palindrome[:i] + "a" + palindrome[i + 1:]
        if i == len(palindrome) - 1: return palindrome[:i] + "b"

    return ""

print(breakPalindrome("aaz"))



