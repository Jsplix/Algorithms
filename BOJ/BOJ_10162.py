import sys
input = sys.stdin.readline
# [BOJ] 10162 전자레인지 / 수학, 구현, 그리디
t = int(input())
if t % 10: print(-1)
else:
    a, b, c = 0, 0, 0
    a = t // 300
    t %= 300
    b = t // 60
    t %= 60
    c = t // 10
    print(a, b, c)