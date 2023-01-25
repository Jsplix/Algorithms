from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline

# [BOJ] 1202 보석 도둑 / 자료 구조, 그리디, 정렬, 우선순위 큐

n, k = map(int, input().split())
jew = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

# 보석을 훔치기 위해서는 [가방의 용량 >= 보석의 무게]가 성립되어야 함.
# 따라서, 가방을 용량에 대해서 오름차순, 보석은 무게에 따른 오름차순으로 정렬되어야 함.
# 가방에 보석을 담을 때는, 위의 정렬 조건으로 인해서 담을 수 있는 보석만 남았으므로, 가치에 대해서 내림차순 정렬함

heapify(jew) # 가방의 용량을 기준으로 우선순위 큐 생성
bag.sort()

ans = 0
temp = []

for c in bag:
    while jew and c >= jew[0][0]: # 해당 가방의 무게보다 작은 보석을 temp에 모두 최대 힙으로 넣음
        heappush(temp, -heappop(jew)[1]) 
        # 가방에 넣을 보석을 찾을 때는 보석의 가치에 -를 붙여서 최대 힙 사용
    if temp: # 1개를 뽑는데 최대 힙이므로 (가장 작은 값이 나올텐데 힙에 추가할 때 -를 붙였으므로 사실상 최대 가치 보석을 뽑는 것)
        # 따라서, 다시 뽑을 때는 -를 붙여서 원래의 가치를 갖도록 해줌 (ans = ans - 보석의 가치 이므로 결국 ans에 보석의 가치를 더하는 연산임)
        ans -= heappop(temp)
    elif not jew: break

print(ans)