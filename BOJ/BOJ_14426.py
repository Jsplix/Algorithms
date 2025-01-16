import sys
input = sys.stdin.readline
# [BOJ] 14426 접두사 찾기 / 자료 구조, 문자열, 트리, 이분 탐색, 트라이
n, m = map(int, input().split())
S = [input().rstrip() for _ in range(n)]
S.sort()

check = [input().rstrip() for __ in range(m)]
check.sort()

result = 0
i, j = 0, 0
while i < n and j < m:
    if S[i][:len(check[j])] == check[j]:
        result += 1
        j += 1
        continue
    if S[i] > check[j]:
        j += 1
        continue
    if S[i] < check[j]:
        i += 1
        continue
    
print(result)