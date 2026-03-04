def distance(lst1 : list[float], lst2 : list[float]) -> float:
    """Calculate the Manhattan distance between 2 points.

    Args:
        lst1 (list[float]): first N dimensional point.
        lst2 (list[float]): second N dimensional point.

    Returns:
        float: the Manhattan distance between the 2 N dimensional points.
    """
    result = 0.0
    for i, j in zip(lst1, lst2, strict=True):
        result += abs(i - j)
    return result