import sys
input = sys.stdin.readline
# [BOJ] 2502 떡 먹는 호랑이 / 수학, DP, 브루트 포스
d, k = map(int, input().split())

arr = [(0, 0), (1, 0), (0, 1)]
for i in range(3, d+1):
    arr.append((arr[i-2][0]+arr[i-2][1], arr[i-1][0]+arr[i-1][1]))

for i in range(1, 100001): # a == i
    if (k - i*arr[d][0]) % arr[d][1] == 0:
        print(i, (k - i*arr[d][0]) // arr[d][1], sep='\n')
        break