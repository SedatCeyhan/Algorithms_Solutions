class Solution:
    def calPoints(self, ops):
        stack = []
        score = 0
        for op in ops:
            if op == "C":
                removed = stack.pop()
                score -= removed
            elif op == "D":
                stack.append(stack[-1] * 2)
                score += stack[-1]
            elif op == "+":
                stack.append(stack[-2] + stack[-1])
                score += stack[-1]
            else:
                stack.append(int(op))
                score += int(op)

        return score

sol = Solution()
op = ["5","-2","4","C","D","9","+","+"]
print(sol.calPoints(op))


