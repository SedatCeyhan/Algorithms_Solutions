# Problem: https://leetcode.com/problems/decode-string/
class Solution:
    def decodeString(self, s):
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                decoded = ""
                while stack[-1] != '[':
                    decoded += stack.pop()

                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k += stack.pop()
                decoded *= int(k[::-1])
                stack.extend(decoded[::-1])

        return "".join(stack)


sol = Solution()
print(sol.decodeString("100[leetcode]"))
