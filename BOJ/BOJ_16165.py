import sys
input = sys.stdin.readline
# [BOJ] 16165 걸그룹 마스터 준석이 / 자료 구조, 해시를 사용한 집합과 맵
n, m = map(int, input().split())
d1, d2 = {}, {}
for i in range(n):
    group = []
    girl_group = input().rstrip()
    mem_n = int(input())
    for i in range(mem_n):
        name = input().rstrip()
        d1[name] = girl_group
        group.append(name)
    d2[girl_group] = sorted(group)

for i in range(m):
    search = input().rstrip()
    k = int(input())

    if k:
        print(d1[search])
    else:
        print(*d2[search], sep = '\n')