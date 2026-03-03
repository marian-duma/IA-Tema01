def distance(lst1 : list[float], lst2 : list[float]) -> float:
    
    distanta = 0.0
    for i, j in zip(lst1, lst2, strict=True):
        distanta += abs(i - j)
    return distanta