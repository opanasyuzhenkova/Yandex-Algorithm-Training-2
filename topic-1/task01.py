# A-Interactor

def solution(returncode, interactor, checker):
    if interactor == 7:
        return 1
    if interactor == 6:
        return 0
    if interactor == 1:
        return checker
    if interactor == 0 and returncode != 0:
        return 3
    if interactor == 0 and returncode == 0:
        return checker
    if interactor == 4 and returncode != 0:
        return 3
    if interactor == 4 and returncode == 0:
        return 4
    return interactor


print(solution(*tuple(map(int, input().split()))))

