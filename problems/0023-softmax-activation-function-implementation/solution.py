import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores = np.array(scores)
    softmax = []

    max_score = np.max(scores)
    exp_sum = 0

    for score in scores:
        exp_sum += np.exp(score - max_score)

    for score in scores:
        softmax.append(np.exp(score - max_score) / exp_sum)

    return softmax