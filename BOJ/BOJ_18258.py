from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 18258 큐 2 / 자료 구조, 큐
queue = deque([])
for _ in range(int(input())):
    comm = list(map(str, input().split()))
    if comm[0] == 'push': queue.append(int(comm[1]))
    elif comm[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif comm[0] == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    elif comm[0] == 'empty':
        if queue: print(0)
        else: print(1)
    elif comm[0] == 'size': print(len(queue))
    elif comm[0] == 'pop': 
        if queue: print(queue.popleft())
        else: print(-1)