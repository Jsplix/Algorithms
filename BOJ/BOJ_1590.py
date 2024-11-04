import sys
input = sys.stdin.readline
# [BOJ] 1590 캠프가는 영식 / 수학, 브루트포스, 이분 탐색
n, t = map(int, input().split())
schedules = [list(map(int, input().split())) for _ in range(n)]

mn = 10**7 + 7
for i in range(n):
    temp = schedules[i][2]
    if t > schedules[i][0] + (temp - 1) * schedules[i][1]: continue
    for j in range(temp):
        if t <= schedules[i][0]:
            mn = min(mn, schedules[i][0] - t)
            break
        schedules[i][0] += schedules[i][1]

if mn == 10**7 + 7: print(-1)
else: print(mn)