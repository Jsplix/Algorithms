import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 1835 카드 / 구현, 자료 구조, 시뮬레이션, 덱
n = int(input())
lst = deque([[0, i] for i in range(1, n+1)])

cnt = 1
answer = deque([])
while lst:
    for i in range(cnt):
        lst.append(lst.popleft())
    lst[0][0] = cnt
    answer.append(lst.popleft())
    cnt += 1

answer = sorted(answer, key=lambda x:x[1])
for num, idx in answer:
    print(num, end=' ')