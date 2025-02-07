import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 12852 1로 만들기 2 / DP, 그래프 이론, 그래프 탐색
def bfs(n):
    global result
    queue = deque()
    queue.append([n])

    while queue:
        temp = queue.popleft()
        x = temp[0]

        if x == 1:
            result = temp
            break

        if x % 3 == 0: queue.append([x // 3] + temp)
        if x % 2 == 0: queue.append([x // 2] + temp)
        queue.append([x - 1] + temp)


result = []
bfs(int(input()))

print(len(result)-1)
print(*result[::-1])