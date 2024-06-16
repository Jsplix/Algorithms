import sys
import heapq
from collections import defaultdict 
input = sys.stdin.readline
# [BOJ] 21939 문제 추천 시스템 Version 1 / 자료 구조, 해시 사용 집합과 맵, 트리 사용 집합과 맵, 우선순위 큐
n = int(input())
maxHeap = []
minHeap = []

# value = 1 (해결 된 문제) / value = 0 (미해결된 문제)
solved = defaultdict(int)

for _ in range(n):
    p, l = map(int, input().split())
    # 동일한 난이도의 경우 문제 번호가 큰 것을 출력하기 위해서 문제 번호도 최대 힙을 만족할 수 있도록 함.
    heapq.heappush(maxHeap, (-l, -p))
    heapq.heappush(minHeap, (l, p))

for __ in range(int(input())):
    comm = list(input().split())
    if comm[0] == 'add':
        comm[1] = int(comm[1])
        comm[2] = int(comm[2])

        heapq.heappush(maxHeap, (-comm[2], -comm[1]))
        heapq.heappush(minHeap, (comm[2], comm[1]))
    elif comm[0] == 'recommend':
        # 우선순위 큐에서 처음, 마지막 원소를 찾아서 pop & push 하는데 시간이 오래걸림
        # 딕셔너리를 활용
        if comm[1] == '1':
            while solved[-maxHeap[0][1]] != 0:
                # 난이도만 변경되어서 다시 입력이 들어올 수 있으므로 해결된 문제는 0으로 바꾸고
                # 우선순위 큐에서 제거해줌
                solved[-maxHeap[0][1]] = 0
                heapq.heappop(maxHeap)
            print(-maxHeap[0][1])
        else:
            while solved[minHeap[0][1]] != 0:
                solved[minHeap[0][1]] = 0
                heapq.heappop(minHeap)
            print(minHeap[0][1])
    else: # solved 명령어 입력된 경우
        solved[int(comm[1])] += 1