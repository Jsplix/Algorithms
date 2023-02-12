from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 16953 A → B / 그래프 이론, 그래프 탐색, DFS, 그리디
a, b = map(int, input().split())
queue = deque([(a, 1)])

while queue:
    x, cnt = queue.popleft()
    if x > b:
        continue
    elif x == b:
        print(cnt)
        exit(0)
    else:
        queue.append((2*x, cnt+1))
        queue.append((int(str(x)+'1'), cnt+1))

print(-1)