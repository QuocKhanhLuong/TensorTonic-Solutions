import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x_arr = np.asarray(x, dtype=float)
    result = np.maximum(0, x_arr)
    return result
    pass