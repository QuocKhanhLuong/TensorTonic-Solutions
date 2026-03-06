import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    x1_arr = np.asarray(x1, dtype=float)
    x2_arr = np.asarray(x2, dtype=float)
    dot = np.dot(x1_arr, x2_arr)
    norm = np.linalg.norm(x1_arr) * np.linalg.norm(x2_arr)
    cos_sim = dot/norm
    if label == 1:
        L = 1 - cos_sim
    elif label == -1:
        L = np.maximum(0, cos_sim - margin)
    return L
    