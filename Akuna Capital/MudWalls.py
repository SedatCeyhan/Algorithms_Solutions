def maxHeight(stickPositions, stickHeights):
    n = len(stickPositions)
    m = len(stickHeights)
    maximum = 0

    for i in range(n - 1):
        if stickPositions[i] < stickPositions[i + 1] - 1:
            heightDiff = abs(stickHeights[i+1] - stickHeights[i])
            gapLen = stickPositions[i + 1] - stickPositions[i] - 1
            localMax = 0
            if gapLen > heightDiff:
                low = max(stickHeights[i + 1], stickHeights[i]) + 1
                remainingGap = gapLen - heightDiff - 1
                localMax = low + remainingGap/2

            else: localMax = min(stickHeights[i+1], stickHeights[i]) + gapLen

            maximum = max(maximum, localMax)

    return int(maximum)

print(maxHeight([1,3,7], [4,3,3]))



