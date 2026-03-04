import random

def check_scale(n : int) -> bool:
    """Check if the scale used is a power of 10.

    Args:
        n (int): the scale by which to shift right the floating point number.

    Returns:
        bool: True if n is a positive power of 10, otherwise False.
    """
    if n <= 0:
        return False
    while n % 10 == 0:
        n //= 10
    return n == 1

def generate_data(seed : int = 3333, size : int = 1000, scale : int = 1) -> list[float]:
    """Generate a random list of numbers.

    Args:
        seed (int, optional): Used to initialise random. Defaults to 3333.
        size (int, optional): The length of the list, or the dimension of
                              the mathematical point. Defaults to 1000.
        scale (int, optional): Upper bound of each random number. Defaults to 1.

    Raises:
        ValueError: the point must have at least 2 dimensions.
        ValueError: the scale should only be a power of 10.

    Returns:
        list[float]: the random generated list of numbers (1 mathematical point).
    """
    random.seed(seed)
    if size < 2:
        raise ValueError("Invalid list size!")
    if not check_scale(scale):
        raise ValueError("Scale must be a power of 10!")
    
    output : list[float] = []
    for _ in range(size):
        output.append(random.random() * scale)
    return output