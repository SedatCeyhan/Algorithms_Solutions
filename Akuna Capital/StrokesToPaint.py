def isValid(i, j, painting, checkChar):
    rows = len(painting)
    cols = len(painting[0])
    return not (i < 0 or j < 0 or i >= rows or j >= cols or painting[i][j] != checkChar)

def dfs(painting, r, c, checkchar):
    painting[r][c] = 'x'
    ith = [0, 1, -1, 0]
    jth = [1, 0, 0, -1]
    for k in range(len(ith)):
        if isValid(r + ith[k], c + jth[k], painting, checkchar):
            dfs(painting, r + ith[k], c + jth[k], checkchar)

def strokesRequired(painting):
    rows = len(painting)
    cols = len(painting[0])

    for p in range(len(painting)):
        temp = painting[p]
        painting[p] = []
        painting[p][:0] = temp

    numberOfComps = 0
    for r in range(rows):
        for c in range(cols):
            if painting[r][c] != 'x':
                numberOfComps += 1
                dfs(painting, r, c, painting[r][c])

    return numberOfComps

print(strokesRequired(["aa","aa"]))