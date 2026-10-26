import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    # Your code here
    ce_losses = np.empty(len(predicted_probs))

    predicted_probs = np.clip(predicted_probs, epsilon, 1)

    for i in range(len(predicted_probs)):
        for j in range(len(predicted_probs[0])):
            if true_labels[i][j] == 1:
                ce_losses[i] = -np.log(predicted_probs[i][j])

    return np.mean(ce_losses)