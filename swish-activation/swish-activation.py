import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x_arr = np.asarray(x, dtype=float)
    sigmoid = 1/(1+np.exp(-x_arr))
    result = x*sigmoid
    return result
    pass