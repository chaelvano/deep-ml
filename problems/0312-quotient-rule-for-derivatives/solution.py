import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g_degree = len(g_coeffs) - 1
    g_derivative = 0
    g = g_coeffs[0]

    for i in range(g_degree):
        g_derivative = g_derivative * x + g
        g = g * x + g_coeffs[i + 1]

    h_degree = len(h_coeffs) - 1
    h_derivative = 0
    h = h_coeffs[0]

    for i in range(h_degree):
        h_derivative = h_derivative * x + h
        h = h * x + h_coeffs[i + 1]

    return (g_derivative * h - g * h_derivative) / h ** 2

