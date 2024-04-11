import sys
from collections import deque 
input = sys.stdin.readline
# [BOJ] 1092 배 / 그리디, 정렬
n = int(input())
crane = sorted(map(int, input().split()), reverse=True)
m = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

# 크레인에 최대한 효율적으로 박스를 옮겨야 함.
# 스케줄링 알고리즘이랑 비슷한 느낌? -> 가벼운거만 먼저 넣는다고 최소 시간이 아님.

# 가장 무게 제한이 큰 크레인이 가장 무거운 박스보다 가벼운 경우, 가장 무거운 짐을 옮길 수 없으므로 -1
if crane[0] < boxes[0]: print(-1)
else:
    cnt = 0
    while boxes:
        for cr in crane:
            if boxes and cr < boxes[-1]: # 크레인 무게 제한이 가장 가벼운 무게보다 작은 경우 continue
                continue
            for bx in boxes:
                if cr >= bx:
                    boxes.remove(bx)
                    break
        cnt += 1
    print(cnt)