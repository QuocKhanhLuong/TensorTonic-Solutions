import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x_arr = np.asarray(x, dtype= float)
    y_arr = np.asarray(y, dtype= float)

    result = np.sqrt(np.sum((x_arr - y_arr)**2))
    return result
    pass