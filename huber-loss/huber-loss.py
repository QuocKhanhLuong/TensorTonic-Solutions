import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y_true_arr = np.asarray(y_true, dtype=float)
    y_pred_arr = np.asarray(y_pred, dtype=float)

    e = y_pred_arr - y_true_arr
    
    L = np.where(np.abs(e) <= delta, 1/2*(e**2),delta*(np.abs(e) - 1/2*delta))
    result = np.mean(L)
    return result
    pass