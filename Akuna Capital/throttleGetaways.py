def findBeforeMatrix(after):
    # Write your code here
    if len(after) == 0 or len(after[0]) == 0: return []
    row, col = len(after), len(after[0])
    before = [[0] * (col) for i in range(row)]
    dict = {}

    # Base case: The 1 dimensional row and column
    before[0][0] = after[0][0]
    for i in range(1, col):
        before[0][i] = after[0][i] - after[0][i - 1]
        dict[i] = before[0][i]

    for j in range(1, row):
        before[j][0] = after[j][0] - after[j - 1][0]

    for i in range(1, row):
        for j in range(1, col):
            val = after[i][j] - after[i][j - 1]
            before[i][j] = val - dict[j]
            dict[j] += before[i][j]

    return before

print(findBeforeMatrix([[1,2], [3,4]]))










def findBeforeMatrix(after):
    # Write your code here
    if len(after) == 0 or len(after[0]) == 0: return []
    row, col = len(after), len(after[0])
    before = [[0] * (col) for i in range(row)]

    # Base case: The 1 dimensional row and column
    before[0][0] = after[0][0]
    for i in range(1, col):
        before[0][i] = after[0][i] - after[0][i - 1]

    for j in range(1, row):
        before[j][0] = after[j][0] - after[j - 1][0]

    for i in range(1, row):
        for j in range(1, col):
            val = after[i][j] - after[i][j - 1]
            for r in range(0, i):
                val -= before[r][j]

            before[i][j] = val

    return before





















import collections
def droppedRequests(requestTime):
    if len(requestTime) <= 3: return 0
    count = collections.Counter(requestTime)
    lookup = collections.defaultdict(int)
    try:
        for i in range(requestTime[0], requestTime[-1] + 1):
            lookup[i] = lookup[i - 1] + count[i]
        for i in range(3, len(requestTime)):
            temp1, temp2 = 0, 0
            if requestTime[i] - 10 in lookup: temp1 = lookup[requestTime[i] - 10]
            if requestTime[i] - 60 in lookup: temp2 = lookup[requestTime[i] - 60]
            if requestTime[i - 3] == requestTime[i]:
                requestTime[i - 3] = '$'
            elif i + 1 - temp1 > 20:
                requestTime[i] = '$'
            elif i + 1 - temp2 > 60:
                requestTime[i] = '$'
        return requestTime.count('$')
    except MemoryError as error:
        return 0







#print(droppedRequests([1,1,1,1,2,2,2,3,3,3,3,4,5,5,5,6,6,6,6,7,7,7,8,8,8,8,9,9,9,9,9,10,10,11,11,11,11,11,11,12,12,12,12,12,12,12,13,13,13,13,14,14,14,14,14,16,16,16,16,16,16,17,17,17,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,20,20,20,20,20]))