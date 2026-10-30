import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.asarray(X, dtype=float)
    dot_prod = X @ X.T
    
    norms = np.linalg.norm(X, axis=1)
    norm_prod = norms[:, None] * norms[None, :]

    S = np.divide(dot_prod, norm_prod, out=np.zeros_like(dot_prod), where=norm_prod != 0)

    return np.round(S, 4).tolist()