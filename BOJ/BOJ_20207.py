import sys
input = sys.stdin.readline
# [BOJ] 20207 달력 / 구현, 그리디, 정렬
calendar = [0 for _ in range(366)]
for _ in range(int(input())):
    s, e = map(int, input().split())
    for x in range(s, e+1): calendar[x] += 1

r, c = 0, 0
result = 0
for schedule in calendar:
    if schedule:
        c = max(c, schedule)
        r += 1
    else:
        result += (r * c)
        r, c = 0, 0

result += (r * c)
print(result)