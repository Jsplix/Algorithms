# [BOJ] 27433 팩토리얼 2 / 수학, 사칙연산
def solve(n):
    if n == 0 or n == 1: return 1
    return n * solve(n-1)
print(solve(int(input())))