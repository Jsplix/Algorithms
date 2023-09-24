import sys
input = sys.stdin.readline
# [BOJ] 29722 브실혜성 / 수학, 구현
year, month, day = map(int, input().split('-'))
n = int(input())

py = year + (n // 360); n %= 360
pm = month + (n // 30); n %= 30
pd = day + n

if pd > 30: pd %= 30; pm += 1
if pm > 12: pm %= 12; py += 1
print(py, str(pm).zfill(2), str(pd).zfill(2), sep='-')