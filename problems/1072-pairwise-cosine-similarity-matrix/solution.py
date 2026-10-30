import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.asarray(X, dtype=float)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    X_norm = np.divide(X, norms, out=np.zeros_like(X), where=norms != 0) 
    S = X_norm @ X_norm.T
    
    return np.round(S, 4).tolist()