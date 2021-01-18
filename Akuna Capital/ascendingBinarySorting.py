def sortByBits(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

def sortByBits2(arr):
    return sorted(arr, key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))

print(sortByBits2([7,8,6,5]))