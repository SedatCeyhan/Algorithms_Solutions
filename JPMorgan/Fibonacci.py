def fib(N):
    if N == 0: return 0
    F = [0] * (N + 1)
    F[1] = 1
    for i in range(2, N + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[-1]

print(fib(6))
