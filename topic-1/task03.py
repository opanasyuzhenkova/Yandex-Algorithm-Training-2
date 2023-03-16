# С-Даты

def is_date_correct(x, y, z) -> int:
    if (x > 12 or y > 12) or (x == y):
        return 1
    return 0


print(is_date_correct(*tuple(map(int, input().split()))))

