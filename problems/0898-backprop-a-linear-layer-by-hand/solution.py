import torch

def linear_backward(grad_output, x, W):
    # TODO: return (grad_input, grad_W, grad_b) for y = x @ W.T + b

    # dy/dx = w
    # dL/dx = dL/dy * dy/dx = dL/dy * w
    grad_input = grad_output @ W

    # dy/dw = x
    # dL/dw = dL/dy * dy/dw = dL/dy * x
    grad_W = grad_output.T @ x

    # dy/db = 1
    # dL/db = dL/dy * dy/db = dL/dy
    grad_b = grad_output.sum(axis=0)

    return (grad_input, grad_W, grad_b)