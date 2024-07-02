import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 16926 배열 돌리기 1 / 구현
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = [[0 for _ in range(m)] for __ in range(n)]
# 껍질 개념으로 1차원으로 바꿔줌 (왼쪽 상단을 기준으로 시계방향으로 1차원 배열 형성)
queue = deque()
for i in range(min(n, m) // 2):
    queue.clear()
    # 상
    queue.extend(arr[i][i:m-i]) 
    # 우
    queue.extend([elem[m-i-1] for elem in arr[i+1:n-i-1]])
    # 하
    queue.extend(arr[n-i-1][i:m-i][::-1])
    # 좌
    queue.extend([elem[i] for elem in arr[i+1:n-i-1][::-1]])

    queue.rotate(-r)

    for j in range(i, m-i):
        result[i][j] = queue.popleft()
    for j in range(i+1, n-i-1):
        result[j][m-i-1] = queue.popleft()
    for j in range(m-i-1, i-1, -1):
        result[n-i-1][j] = queue.popleft()
    for j in range(n-i-2, i, -1):
        result[j][i] = queue.popleft()
    
for row in result:
    print(*row)