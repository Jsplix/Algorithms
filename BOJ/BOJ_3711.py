import sys
input = sys.stdin.readline
# [BOJ] 3711 학번 / 수학, 브루트포스, 정수론, 집합과 맵
for _ in range(int(input())):
    g = int(input())
    stid = [int(input()) for __ in range(g)]
    for i in range(1, 10**6):
        temp = set()
        for id in stid:
            if id % i in temp: break
            temp.add(id % i)
        
        if len(temp) == g:
            m = i
            break
    print(m)