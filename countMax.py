import math

def countMax(upRight):
    # Write your code here
    row = math.inf
    col = math.inf

    for i in range(len(upRight)):
        rowCol = upRight[i].split(" ")
        curr_row = int(rowCol[0])
        curr_col = int(rowCol[1])
        if curr_row < row:
            row = curr_row
        if curr_col < col:
            col = curr_col

    return row * col

print(countMax(["1 4", "2 3", "4 1"]))




