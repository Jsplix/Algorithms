import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 12851 숨바꼭질 2 / 그래프 이론, 그래프 탐색, BFS
def bfs(start, target): # start ~ target의 BFS
    global possible
    if start == target: possible.append(0) ; return # 시작점과 일치하다면 0 추가 후 함수 종료

    road[start] = 0 # 시작점의 cnt 횟수는 0으로 시작
    queue = deque([start])

    while queue: # BFS 실행
        now = queue.popleft()
        for next in [2 * now, now + 1, now - 1]: # 이동 방법 총 3가지.
            if next < 0:  # 범위를 벗어나거나 이미 방문했던 곳이라면 continue
                continue

            if next > target: # target 보다 먼 곳에 위치하다면 → -1씩 가야하므로 한 번에 계산해줌
                possible.append(road[now] + (next - target) + 1)
                continue
            elif next == target: # 현재 위치가 target이라면 시간 possible에 저장하고 continue
                possible.append(road[now] + 1)
                continue
            else: # 그 외
                if road[next] == -1: # 방문하지 않은 곳 → 없어도 되는 부분이긴 할 듯.
                    queue.append(next) # 큐에 넣어줌
                    road[next] = road[now] + 1 # 시간 갱신.
                else:
                    if road[next] >= road[now] + 1: # 기존에 방문한 시간이 현재보다 길다면 갱신해줌.
                        road[next] = road[now] + 1
                        queue.append(next)
    
    return 

LIMIT = 10**6 + 1
n, k = map(int, input().split())
road = [-1 for _ in range(LIMIT)]

possible = []
bfs(n, k)
mn_time = min(possible) # 최소 시간 확인
mn_cnt = possible.count(mn_time) # 최소 시간이 몇 번인지 확인

print(mn_time, mn_cnt, sep='\n')