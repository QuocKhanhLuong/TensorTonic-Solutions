import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x_arr = np.asarray(x, dtype=float)
    max_x = np.max(x, axis=-1, keepdims=True)
    shift_x = x_arr - max_x
    exp_x = np.exp(shift_x)
    result = exp_x / np.sum(exp_x, axis=-1, keepdims=True)
    return result
    pass