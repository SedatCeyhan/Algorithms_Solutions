import collections
import math

def minSetSize(arr):
    # In Python, we can use the built-in Counter class.
    counts = collections.Counter(arr)

    # Extract the counts in reverse-sorted order.
    # most_common gives (number, count) pairs, reverse sorted on count.
    counts = [count for number, count in counts.most_common()]

    # Remove numbers until at least half are removed.
    total_removed = 0
    set_size = 0
    for count in counts:
        total_removed += count
        set_size += 1
        if (total_removed >= math.ceil(len(arr)/2)):
            break

    return set_size

print(minSetSize([3, 4, 6, 11, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8]))


