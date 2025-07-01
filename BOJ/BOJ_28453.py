import sys
input = sys.stdin.readline
# [BOJ] 28453 Previous Level / 구현, 많은 조건 분기
n = int(input())
levels = list(map(int, input().split()))

result = []
for level in levels:
    if level < 250: result.append(4)
    elif 250 <= level < 275: result.append(3)
    elif 275 <= level < 300: result.append(2)
    elif level == 300: result.append(1)
print(*result)