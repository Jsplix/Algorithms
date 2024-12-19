import sys
input = sys.stdin.readline
# [BOJ] 30999 민주주의 / 구현, 문자열
n, m = map(int, input().split())
votes = [input().rstrip() for _ in range(n)]

result = 0
for i in range(n):
    if votes[i].count('O') >= (m + 1) // 2: result += 1
print(result)