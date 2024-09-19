import sys
input = sys.stdin.readline
# [BOJ] 17827 달팽이 리스트 / 수학, 구현
n, m, v = map(int, input().split())
val = list(map(int, input().split()))

next_node = [i+1 for i in range(1, n+1)]
next_node[-1] = v

for i in range(m):
    q = int(input())
    if q <= n:
        print(val[next_node[q-1]-1])
    else:
        idx = q - v + 1
        k = v - 1 # v번 노드 앞까지는 사이클에 포함되지 않음.
        print(val[k + (idx % (n - k))])