import sys
input = sys.stdin.readline

# [BOJ] 1647 도시 분할 계획 / 그래프 이론, 최소 스패닝 트리(MST)

n, m = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(m)]
path.sort(key=lambda x: x[2])
vRoot = [i for i in range(100001)]

def find(x):
    if vRoot[x] != x: vRoot[x] = find(vRoot[x])
    return vRoot[x]

answer = 0
selected = []
for v1, v2, e in path:
    Root_1 = find(v1)
    Root_2 = find(v2)
    if Root_1 != Root_2:
        if Root_1 < Root_2: vRoot[Root_2] = Root_1
        else: vRoot[Root_1] = Root_2
        answer += e
        selected.append(e)

# 추가된 간선 중 마지막으로 추가 된 간선을 제거하여 마을을 2개로 분리시킨다.
# 마지막으로 추가 된 간선을 제거하는 이유는 간선을 가중치를 기준으로 오름차순 정렬한 상태에서 추가했기 때문에
# 해당 간선의 가중치가 가장 크기 때문이다.
selected.pop()
print(sum(selected))