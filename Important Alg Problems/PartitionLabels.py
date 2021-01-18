def partitionLabels(S):
    last = {c:i for i, c in enumerate(S)}
    left, right = 0, 0
    partitions = []

    for i, c in enumerate(S):
        right = max(right, last[c])
        if right == i:
            partitions.append(right - left + 1)
            left = right + 1

    return partitions


print(partitionLabels("sedeatakolol"))