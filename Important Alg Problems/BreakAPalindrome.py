'''
Given a palindromic string palindrome, replace exactly one character by any lowercase English letter
so that the string becomes the lexicographically smallest possible string that isn't a palindrome.
After doing so, return the final string.  If there is no way to do so, return the empty string.

'''

class Solution:
    def breakPalindrome(self, palindrome):
        n = len(palindrome)
        if n <= 1: return ""

        for i in range(n):
            if palindrome[i] != 'a':
                if i != n - 1 - i:
                    return palindrome[:i] + 'a' + palindrome[i+1:]
                else:
                    return palindrome[:-1] + 'b'
        return palindrome[:-1] + 'b'



class Solution2:
    def breakPalindrome(self, palindrome):
        if not palindrome or len(palindrome) == 1: return ""
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                if i != len(palindrome) - 1 - i: return palindrome[:i] + "a" + palindrome[i + 1:]
            if i == len(palindrome) - 1: return palindrome[:i] + "b"

sol = Solution()
print(sol.breakPalindrome("abccba"))
