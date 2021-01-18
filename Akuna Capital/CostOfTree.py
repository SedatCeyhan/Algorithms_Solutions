def mctFromLeafValues(self, arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    self.memo = {}

    def dp(i, j):
        if j <= i:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        res = float('inf')
        for k in range(i, j):
            res = min(res, dp(i, k) + dp(k + 1, j) + (max(arr[i:k + 1]) * max(arr[k + 1:j + 1])))
        self.memo[(i, j)] = res
        return self.memo[(i, j)]

    return dp(0, len(arr) - 1)