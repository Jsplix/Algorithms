import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 24511 queuestack / 자료 구조, 스택, 덱, 큐
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = deque([])
for i in range(N):
    if A[i]: continue
    queue.append(B[i])

for j in range(M):
    queue.appendleft(C[j])
    print(queue.pop(), end=' ')