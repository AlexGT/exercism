def score(x, y):
    sq_distance = (x**2 + y**2) ** 0.5
    
    if sq_distance <= 1:
        return 10
    if sq_distance <= 5:
        return 5
    if sq_distance <= 10:
        return 1
    return 0
