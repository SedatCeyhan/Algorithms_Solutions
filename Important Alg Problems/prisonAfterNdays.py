from collections import defaultdict

def prisonAfterNDays(cells, N):
    if N == 0: return cells
    cellsDict = defaultdict(lambda: -1)
    cellsDict[tuple(cells)] = 0
    for day in range(1, N + 1):
        temp = [0]
        for c in range(1, 7):
            if cells[c - 1] == cells[c + 1]:
                temp.append(1)
            else: temp.append(0)

        temp.append(0)
        cells = temp
        if cellsDict[tuple(cells)] > -1:
            C = day - cellsDict[tuple(cells)]
            r = (N - day) % C
            return list(cellsDict.keys())[r + cellsDict[tuple(cells)]]

        cellsDict[tuple(cells)] = day

    return cells

print(prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
