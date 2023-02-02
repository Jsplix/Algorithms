import sys
input = sys.stdin.readline
# [BOJ] 13567 로봇 / 구현, 시뮬레이션
m, n = map(int, input().split())
x, y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 0이 들어오면 index를 +1, 1이 들어오면 -1 해줌
d = 0
flag = False

for i in range(n):
    comm = input().split()
    if comm[0] == 'MOVE':
        x += dx[d]*int(comm[1])
        y += dy[d]*int(comm[1])
        if x < 0 or y < 0 or x > m or y > m:
            flag = True
    else:
        if comm[1] == '0':
            if d == 3: d = 0
            else: d += 1
        else:
            if d == 0: d = 3
            else: d -= 1

if x < 0 or y < 0 or x > m or y > m or flag: print(-1)
else: print(x, y)