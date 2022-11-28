from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 1021 회전하는 큐 / 자료 구조, 덱
n, m = map(int, input().split())
pop_list = list(map(int, input().split()))
l = deque([ i for i in range(1, n + 1) ])
idx = 0
cnt = 0
while m:
    left_dist = l.index(pop_list[idx])
    right_dist = len(l) - left_dist
    if left_dist <= right_dist:
        for _ in range(left_dist):
            cnt += 1
            l.append(l.popleft())
    else:
        for _ in range(right_dist):
            cnt += 1
            l.appendleft(l.pop())
    l.popleft()
    m -= 1
    idx += 1
print(cnt)