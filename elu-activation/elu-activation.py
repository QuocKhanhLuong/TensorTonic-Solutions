import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x_arr = np.asarray(x, dtype=float)
    result = np.where(x_arr > 0, x_arr, alpha*(np.exp(x_arr)-1))
    ans = result.tolist()
    return ans