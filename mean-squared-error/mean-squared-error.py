import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred_arr = np.asarray(y_pred, dtype=float)
    y_true_arr = np.asarray(y_true, dtype=float)
    if y_pred_arr.shape != y_true_arr.shape: return None
    squared_diff = (y_pred_arr - y_true_arr) ** 2
    result = float(np.mean(squared_diff))
    return result
    pass
