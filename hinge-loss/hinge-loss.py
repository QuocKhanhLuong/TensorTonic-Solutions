import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    Compute the Hinge Loss for binary classification.
    """
    y = np.asarray(y_true, dtype=float)
    s = np.asarray(y_score, dtype=float)
    
    losses = np.maximum(0, margin - y * s)
    
    if reduction == "mean":
        result = losses.mean()
    elif reduction == "sum":
        result = losses.sum()
    else:
        raise ValueError()
        
    return float(result)