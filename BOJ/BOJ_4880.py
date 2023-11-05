import sys
input = sys.stdin.readline
# [BOJ] 4880 다음수 / 수학, 사칙연산
while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == 0 and a2 == 0 and a3 == 0: break
    if abs(a1-a2) == abs(a2-a3):
        print("AP", a3 + (a3 - a2))
    else:
        print("GP", a3 * (a3 // a2))