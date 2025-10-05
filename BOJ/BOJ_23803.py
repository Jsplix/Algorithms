import sys
input = sys.stdin.readline
# [BOJ] 23803 골뱅이 찍기 - ㄴ / 구현
n = int(input())
result = []
for _ in range(4 * n):
    result.append(['@' * n])
for __ in range(n):
    result.append(['@' * 5 * n])

for i in range(len(result)):
    print(*result[i])