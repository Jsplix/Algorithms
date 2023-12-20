from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 17503 맥주 축제 / 자료 구조, 그리디, 정렬, 우선순위 큐, 이분 탐색
n, m, k = map(int, input().split())
preferences = [list(map(int, input().split())) for _ in range(k)] # 선호도, 도수 레벨
preferences.sort(key= lambda x:(x[1]))
liver, day, val = 0, 0, 0 # 간 레벨, 맥주 마신 일 수, 현재까지의 선호도

chk = []
for i in range(k):
    if day + 1 <= n:
        day += 1
        val += preferences[i][0]
        liver = max(liver, preferences[i][1])
        heappush(chk, (preferences[i][0], preferences[i][1]))
    
    if day == n:
        if val >= m: break
        else:
            day -= 1
            k = heappop(chk)
            val -= k[0]
            liver = 0 if len(chk) == 0 else chk[0][1]

if val >= m: print(liver)
else: print(-1)