# D-Строительство школы
from statistics import median


def find_school_coordinates(n: int, houses: list) -> int:
    return int(median(houses))


n = int(input())
houses = list(map(int, input().split()))
print(find_school_coordinates(n, houses))
