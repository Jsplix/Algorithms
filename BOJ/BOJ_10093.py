import sys
input = sys.stdin.readline
# [BOJ] 10093 숫자 / 구현
a, b = map(int, input().split())
result = [v for v in range(min(a,b)+1, max(a,b))]
print(len(result))
print(*result)