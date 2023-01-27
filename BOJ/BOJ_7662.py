from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 7662 이중 우선순위 큐 / 자료 구조, 우선순위 큐
# 문제 이름처럼 우선순위 큐(힙)을 2개 써야함. (파이썬 내장 힙은 기본이 최소힙임)
for _ in range(int(input())): # tc 입력받기
    k = int(input())
    min_Q, max_Q = [], []
    chk = [0 for _ in range(k)]
    for i in range(k):
        comm = input().rstrip().split()
        if comm[0] == 'I':
            heappush(min_Q, (int(comm[1]), i))
            heappush(max_Q, (-int(comm[1]), i))
            chk[i] = 1
        else:
            if comm[1] == '-1': # 최솟값 삭제
                while min_Q and not chk[min_Q[0][1]]:
                    heappop(min_Q)
                if min_Q:
                    chk[min_Q[0][1]] = 0
                    heappop(min_Q)
            else: # 최댓값 삭제
                while max_Q and not chk[max_Q[0][1]]:
                    heappop(max_Q)
                if max_Q:
                    chk[max_Q[0][1]] = 0
                    heappop(max_Q)
    # 동기화 // => 제거를 할 때, 각각 최대힙, 최소힙에서 제거하므로 최종적으로는
    # chk 리스트를 통해서 두 힙을 똑같이 만들어주기 위해서 다른 부분은 제거함.
    while min_Q and not chk[min_Q[0][1]]:
        heappop(min_Q)
    while max_Q and not chk[max_Q[0][1]]:
        heappop(max_Q)
    
    if not min_Q or not max_Q:
        print("EMPTY")
    else:
        print(-max_Q[0][0], min_Q[0][0]) # 최대힙은 양수값을 음수로 바꿔 넣었으므로 다시 -를 곱해줌