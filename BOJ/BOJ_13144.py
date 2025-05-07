import sys
input = sys.stdin.readline
# [BOJ] 13144 List of Unique Numbers / 투 포인터
n = int(input())
arr = list(map(int, input().split()))

visited = [0 for _ in range(10**5+7)]
i, j = 0, 0
result = 0
while i <= j and j < n:
    if not visited[arr[j]]:
        visited[arr[j]] = 1
        j += 1
        result += j - i
    else:
        while visited[arr[j]]:
            visited[arr[i]] = 0
            i += 1

print(result)