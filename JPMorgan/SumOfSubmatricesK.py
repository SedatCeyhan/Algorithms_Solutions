def sumOfSubmatrices(matrix, k):
    if not matrix: return []
    rows, cols = len(matrix), len(matrix[0])
    k_matrix = []
    for r in range(rows - k + 1):
        k_matrix_row = []
        for c in range(cols - k + 1):
            total = 0
            for i in range(r, r + k):
                total += sum(matrix[i][c:c + k])
            k_matrix_row.append(total)
        k_matrix.append(k_matrix_row)

    return k_matrix

k_matrix = sumOfSubmatrices([[1,2,3],
                             [4,5,6],
                             [7,8,9]], 5)

for r in k_matrix:
    print(r)
