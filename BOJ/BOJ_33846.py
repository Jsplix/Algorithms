import sys
input = sys.stdin.readline
# [BOJ] 33846 삽입 정렬을 해볼까 / 정렬
n, t = map(int, input().split())
temp = []
arr = list(map(int, input().split()))

for i in range(t):
    temp.append(arr[i])
temp.sort()

temp.extend(arr[t:])
print(*temp)