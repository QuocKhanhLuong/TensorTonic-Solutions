import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v_arr = np.asarray(v, dtype = float)
    if v_arr.ndim == 1:
        norm = np.sqrt(np.sum(v_arr**2))
        if norm == 0:
            return v_arr
        else:
            vec = v_arr / norm
            return vec
    if v_arr.ndim == 2:
        norms = np.sqrt(np.sum(v_arr**2, axis=1, keepdims=True))
        norms_safe = np.where(norms == 0, 1.0, norms)
        
        return v_arr / norms_safe   
    pass