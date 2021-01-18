def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n - 1, k) + (k - 1)) % n + 1

print(josephus(7,5))