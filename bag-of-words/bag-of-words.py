import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    vocab_dict = {word: i for i, word in enumerate(vocab)}
    counts = np.zeros(len(vocab), dtype=int)
    for token in tokens:
        if token in vocab_dict:
            index = vocab_dict[token]
            counts[index] += 1
            
    return counts
    pass