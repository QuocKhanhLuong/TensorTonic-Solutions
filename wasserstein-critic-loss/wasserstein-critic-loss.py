import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    r = np.asarray(real_scores)
    f = np.asarray(fake_scores)
    r_mean = np.mean(r)
    f_mean = np.mean(f)
    result = f_mean - r_mean
    return result
    pass