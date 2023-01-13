import sys
input = sys.stdin.readline
# [BOJ] 1629 곱셈 / 수학, 분할 정복, 재귀
# 나머지 분배 법칙 - (A*B)%C = (A%C)*(B%C)%C
def solve(base, exp):
    global c
    if exp == 1:
        return base%c
    else:
        k = solve(base, exp//2)
        if exp % 2:
            return (k*k*base)%c
        else:
            return (k*k)%c

a, b, c = map(int, input().split())
print(solve(a,b))