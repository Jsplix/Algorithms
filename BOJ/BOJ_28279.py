import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 28279 덱 2 / 자료 구조, 덱
n = int(input())
deq = deque([])
for _ in range(n):
    comm = list(map(int, input().split()))
    if comm[0] == 1:
        deq.appendleft(comm[1])
    elif comm[0] == 2:
        deq.append(comm[1])
    elif comm[0] == 3:
        if deq: print(deq.popleft())
        else: print(-1)
    elif comm[0] == 4:
        if deq: print(deq.pop())
        else: print(-1)
    elif comm[0] == 5:
        print(len(deq))
    elif comm[0] == 6:
        if deq: print(0)
        else: print(1)
    elif comm[0] == 7:
        if deq: print(deq[0])
        else: print(-1)
    elif comm[0] == 8:
        if deq: print(deq[-1])
        else: print(-1)
