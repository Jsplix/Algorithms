import sys
input = sys.stdin.readline
# [BOJ] 12805 트리 나라 관광 가이드 / 그래프 이론, 그래프 탐색, 트리, 집합과 맵
K = int(input())
seq = list(map(int, input().split()))

parents = [-1 for _ in range(K)]
path = set([seq[0]])

count = 1
for i in range(1, K):
    if seq[i] not in path:
        parents[seq[i]] = seq[i - 1]
        path.add(seq[i])
    else:
        continue

count = max(seq) + 1
print(count)
print(*parents[:count])