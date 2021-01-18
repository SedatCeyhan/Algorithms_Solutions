class Solution:
    def calPoints(self, ops):
        sum = 0
        stack = []
        for r in ops:
            if r == "C":
                inv = stack.pop(-1)
                sum -= inv
            elif r == "D":
                new_rnd = stack[-1] * 2
                stack.append(new_rnd)
                sum += new_rnd
            elif r == "+":
                new_rnd = stack[-1] + stack[-2]
                stack.append(new_rnd)
                sum += new_rnd
            else:
                stack.append(int(r))
                sum += int(r)

        return sum



    def backspaceCompare(self, S, T):
        strS, strT = "", ""
        for c in S:
                if c == "#":
                    if strS:
                        strS = strS[:-1]
                else: strS += str(c)

        for c in T:
                if c == "#":
                    if strT:
                        strT = strT[:-1]
                else:
                    strT += str(c)

        return strS == strT


