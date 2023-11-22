import sys
input = sys.stdin.readline
# [BOJ] 2565 경비원 / 구현, 많은 조건 분기
n, m = map(int, input().split())
s = int(input())
stores = [tuple(map(int, input().split())) for _ in range(s)]
dong = tuple(map(int, input().split()))

g = 0
for i in range(s):
    d, p = stores[i]
    if d == dong[0]: # 같은 라인에 있음
        g += abs(dong[1]-p)
    else: # 다른 라인에 있음
        if d == 1:
            if dong[0] == 2: g += min(m + dong[1] + p, m + (n-dong[1]) + (n-p))
            elif dong[0] == 3: g += p + dong[1]
            elif dong[0] == 4: g += (n-p) + dong[1]
        elif d == 2:
            if dong[0] == 1: g += min(m + dong[1] + p, m + (n-dong[1]) + (n-p))
            elif dong[0] == 3: g += ((m-dong[1]) + p)
            elif dong[0] == 4: g += ((m-dong[1]) + (n-p))
        elif d == 3:
            if dong[0] == 1: g += p + dong[1]
            elif dong[0] == 2: g += (m-p) + dong[1]
            elif dong[0] == 4: g += min(n + p + dong[1], n + (m-p) + (m-dong[1]))
        else:
            if dong[0] == 1: g += p + n-dong[1]
            elif dong[0] == 2: g += (m-p) + (n-dong[1])
            elif dong[0] == 3: g += min(n + p + dong[1], n + (m-p) + (m-dong[1]))
print(g)