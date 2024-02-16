import sys
input = sys.stdin.readline
# [BOJ] 10159 저울 / 그래프 이론, 그래프 탐색, 최단 경로, 플로이드 워셜
def solution(depth, now, lst: list, path):
    
    if not len(lst[now]):
        return depth

    cnt = 0
    for next in lst[now]:
        if next not in path:
            path.append(next)
            cnt += solution(depth + 1, next, lst, path)

    return len(path) - 1

n = int(input())
m = int(input())

heavy, light = [[] for _ in range(n+1)], [[] for _ in range(n+1)]
# heavy에는 각 번호보다 무거운 것을, light에는 각 번호보다 가벼운 것을 저장
for _ in range(m):
    a, b = map(int, input().split())
    light[a].append(b)
    heavy[b].append(a)

for i in range(1, n + 1):
    l = solution(0, i, light, [i])
    h = solution(0, i, heavy, [i])
    print(n - (l + h + 1))