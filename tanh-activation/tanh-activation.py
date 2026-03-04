import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x_arr = np.asarray(x, dtype=float)
    result =  (np.exp(x_arr) - np.exp(-x_arr))/(np.exp(x_arr) + np.exp(-x_arr))
    return result
    
    pass