import sys
input = sys.stdin.readline
# [BOJ] 2776 암기왕 / 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    d = {}
    for x in a:
        d[x] = 1

    m = int(input())
    b = list(map(int, input().split()))

    for i in range(m):
        if b[i] in d:
            print(1)
        else:
            print(0)