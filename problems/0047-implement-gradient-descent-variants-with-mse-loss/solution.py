import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # Your code here
    # dL/dw = dL/de * de/dy_hat * dy/dw
    # dL/dw = d/de e^2 * d/dy_hat y_hat - y * d/dw wX
    # dL/dw = 2e * 1 * X
    if method == 'stochastic':
        for _ in range(n_epochs):
            for sample, target in zip(X, y):
                weights -= learning_rate * 2 * (sample @ weights - target) * sample
    elif method == 'mini_batch':
        for _ in range(n_epochs):
            for i in range(0, X.shape[0], batch_size):
                batch = X[i:i + batch_size]
                target = y[i:i + batch_size]

                weights -= learning_rate * 2 * (batch @ weights - target) / batch.shape[0] @ batch
    else:
        n = X.shape[0]

        for _ in range(n_epochs):
            weights -= learning_rate * 2 * (X @ weights - y) / n @ X

    return weights