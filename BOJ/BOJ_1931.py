import sys
input = sys.stdin.readline
# [BOJ] 1931 회의실 배정 / 그리디, 정렬
n = int(input())
schedule = []
for _ in range(n):
    schedule.append(tuple(map(int, input().split())))
schedule.sort(key=lambda x:(x[1], x[0]))

time = schedule[0][1]
cnt = 1
for i in range(1, n):
    if time <= schedule[i][0]:
        time = schedule[i][1]
        cnt += 1
print(cnt)