import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    n = len(A)
    m = len(A[0])

    transposed = np.zeros((m, n), dtype=int)

    for i in range(n):
        for j in range(m):
            transposed[j][i] = A[i][j]

    return transposed
    pass
