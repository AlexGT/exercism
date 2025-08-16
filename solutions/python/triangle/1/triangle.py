def is_valid_triangle(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0:
        return a + b >= c and b + c >= a and a + c >= b
    return False


def equilateral(sides):
    if is_valid_triangle(sides):
        return len(set(sides)) == 1
    return False


def isosceles(sides):
    if is_valid_triangle(sides):
        return len(set(sides)) <= 2
    return False
    

def scalene(sides):
    if is_valid_triangle(sides):
        return len(set(sides)) == 3
    return False
