import sys
input = sys.stdin.readline
# [BOJ] 2979 트럭 주차 / 구현, 시뮬레이션
a, b, c = map(int, input().split())
trucks = [list(map(int, input().split())) for _ in range(3)]
trucks.sort()

times = [0 for _ in range(101)]

arrive, leave = 101, -1
for s, e in trucks:
    arrive = min(arrive, s)
    leave = max(leave, e)
    for i in range(s, e):
        times[i] += 1

total = 0
for i in range(arrive, leave):
    if times[i] == 1:
        total += a
    elif times[i] == 2:
        total += (2*b)
    elif times[i] == 3:
        total += (3*c)

print(total)