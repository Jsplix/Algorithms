import sys
input = sys.stdin.readline
# [BOJ] 1043 거짓말 / 자료 구조, 그래프 이론, 그래프 탐색, 분리 집합
n, m = map(int, input().split())
know = set(input().split()[1:])
party = [set(input().split()[1:]) for _ in range(m)]

for _ in range(m):
    for i in range(m):
        if know & party[i]: know = know.union(party[i])

answer = 0
for i in range(len(party)):
    if know & party[i]: continue
    answer += 1

print(answer)