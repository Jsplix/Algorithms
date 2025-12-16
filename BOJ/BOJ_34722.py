import sys
input = sys.stdin.readline
# [BOJ] 34722 출제자가 몇 명 / 구현
result = 0
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a >= 1000 or b >= 1600 or c >= 1500 or (d != -1 and d <= 30):
        result += 1
print(result)