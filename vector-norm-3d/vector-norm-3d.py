import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    v_arr = np.asarray(v, dtype = float)
    if v_arr.ndim == 1:
        norm = np.sqrt(np.sum(v_arr**2))
        return norm
    if v_arr.ndim == 2:
        norms = np.sqrt(np.sum(v_arr**2, axis=1))
        return norms
    pass