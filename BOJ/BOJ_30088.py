import sys
input = sys.stdin.readline
# [BOJ] 30088 공포의 면담실 / 그리디, 정렬, 누적합
schedules = [[i] + list(map(int, input().split())) for i in range(1, int(input()) + 1)]
schedules.sort(key = lambda x: sum(x[2:]))

total, prev = 0, 0
for schedule in schedules:
    prev += sum(schedule[2:])
    total += prev
print(total)