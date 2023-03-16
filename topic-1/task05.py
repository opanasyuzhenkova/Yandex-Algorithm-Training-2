# E-Точка и треугольник

def euqlidian_distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)** 2

def location(d: int, x: int, y:int) -> int:
    if x >= 0 and y >= 0 and y <= d - x:
        return 0
    distance = ([euqlidian_distance(0, 0, x, y), euqlidian_distance(d, 0, x, y), euqlidian_distance(0, d, x, y)])

    return distance.index(min(distance)) + 1

print(location(4, 4, 4))

