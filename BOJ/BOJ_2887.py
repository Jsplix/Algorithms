import sys
input = sys.stdin.readline
# [BOJ] 2887 행성 터널 / 그래프 이론, 정렬, 최소 스패닝 트리(MST)
def find(x):
    if x != vrtx[x]:
        vrtx[x] = find(vrtx[x])
    return vrtx[x]

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    vrtx[v2] = v1

x_pos, y_pos, z_pos = [], [], []
n = int(input())
for planet in range(n):
    x, y, z = map(int, input().split())
    x_pos.append((x, planet))
    y_pos.append((y, planet))
    z_pos.append((z, planet))

x_pos.sort()
y_pos.sort()
z_pos.sort()

weights = []
for pos in x_pos, y_pos, z_pos:
    for i in range(1, n):
        e1, p1 = pos[i-1]
        e2, p2 = pos[i]
        weights.append((abs(e1-e2), p1, p2))
        # p1, p2 행성 사이의 가중치 저장
weights.sort(reverse=True) # 가중치가 큰 순서로 정렬

vrtx = [i for i in range(n+1)]
answer, chk = 0, n-1
while chk:
    w, p1, p2 = weights.pop()
    if find(p1) == find(p2): continue
    union(p1, p2)
    answer += w
    chk -= 1
print(answer)