# B-Кольцевая линия

def solution(n: int, i: int, j: int) -> int:
    return min(abs(j-i) - 1, n - max(i,j) + min(i, j) - 1)


print(solution(*tuple(map(int, input().split()))))
