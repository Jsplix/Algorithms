from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 16397 탈출 / 그래프 이론, 그래프 탐색, BFS
def bfs():
    global n, t, g
    queue = deque([(n, 0)])

    while queue:
        now, cnt = queue.popleft()
        
        if now == g: return cnt
        if cnt >= t: continue

        for next in [now + 1, 2 * now - (10**(len(str(2 * now))-1)) if 2 * now < 10**5 else -1]:
            if next == -1 or next > 99999: continue # 탈출 실패
            if not visited[next]:
                if next == g: return cnt + 1
                visited[next] = 1
                queue.append((next, cnt + 1))

    return "ANG"

n, t, g = map(int, input().split())
visited = [0 for _ in range(10**6)]
visited[n] = 1

print(bfs())