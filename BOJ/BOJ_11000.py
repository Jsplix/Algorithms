import sys
import heapq
input = sys.stdin.readline
# [BOJ] 11000 강의실 배정 / 자료 구조, 그리디, 정렬, 우선순위 큐

# 빨리 시작하는 순서로 정렬해줌. 

# 현재 강의 종료 시간이 다음 강의 시작 시간보다 빠를 경우 -> 강의실을 개설할 필요 X
# 현재 강의 종료 시간이 다음 강의 시작 시간보다 느릴 경우 -> 강의실 개설 O
n = int(input())
schedules = [list(map(int, input().split())) for _ in range(n)]
schedules.sort(key= lambda x: (x[0], x[1]))

pq = [schedules[0][1]]
for i in range(1, n):
    if pq[0] <= schedules[i][0]:
        heapq.heappop(pq) # 기존의 강의실 그대로 사용.
    # 윗 줄에서 pop이 된 경우, 강의실 사용 시간을 연장 / pop이 되지 않은 경우 강의실을 개설한 경우
    heapq.heappush(pq, schedules[i][1]) 

print(len(pq))