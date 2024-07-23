import sys
input = sys.stdin.readline
# [BOJ] 14569 시간표 짜기 / 구현, 브루트포스, 비트마스킹
n = int(input())
subjects = []
for _ in range(n):
    x, *t = map(int, input().split())
    subjects.append(set(t))

m = int(input())
schedules = []
for _ in range(m):
    x, *s = map(int, input().split())
    schedules.append(set(s))

for i in range(m):
    count = 0
    for j in range(n):
        if schedules[i].intersection(subjects[j]) == subjects[j]:
            count += 1
    print(count)