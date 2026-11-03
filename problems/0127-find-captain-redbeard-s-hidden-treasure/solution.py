def find_treasure(x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

  Returns:
        float: The x-coordinate of the minimum point.
    """
    # Your code here
    n_iterations = 2000
    learning_rate = 0.01
    momentum_coefficient = 0.9

    velocity = 0

    for _ in range(n_iterations):
      gradient = 4 * x ** 3 - 9 * x ** 2
      velocity = momentum_coefficient * velocity + gradient

      x -= learning_rate * velocity

    return x

