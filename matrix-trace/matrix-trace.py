import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    n = len(A) 
    result = 0.0
    for i in range(n):
        result += A[i][i]

    return result
    pass
