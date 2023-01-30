from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 20301 반전 요세푸스 / 구현, 자료 구조, 시뮬레이션, 덱
# ※ Python3으로 제출할 경우 추가 시간이 없기 때문에 TLE 발생하므로 Pypy로 제출하여야 함.
n, k, m = map(int, input().split())
queue = deque([i for i in range(1, n+1)])

temp = []
idx, cnt = 1, 0
rev = False

while cnt != n:
    if idx == k: 
        if not rev: temp.append(queue.popleft())
        else: temp.append(queue.pop())
        idx = 0
        cnt += 1
        if cnt and not cnt % m:
            if not rev: rev = True
            else: rev = False
    else: 
        if not rev: queue.append(queue.popleft())
        else: queue.appendleft(queue.pop())
    idx += 1

print('\n'.join(map(str, temp)))