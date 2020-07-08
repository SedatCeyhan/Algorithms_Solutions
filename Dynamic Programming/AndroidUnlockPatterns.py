def numberOfPatterns(m, n):
    def isValid(start, end):
        if used[end] == 1: return False
        if (start + end) % 2 == 1: return True



        return

    def calcPatterns(start, l):
        sum = 0
        for i in range(1, 10):
            if isValid(start, i):
                used[i] = 1
                sum += calcPatterns(i, l - 1)
                used[i] = 0

        return sum



    sum = 0
    for l in range(m, n + 1):
        for start in range(1, 10):
            used = [0] * 10
            used[start] = 1
            sum += calcPatterns(start, l - 1)



x = sum([x*x for x in [1,2,3]])
print(x)