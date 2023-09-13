import sys
input = sys.stdin.readline
# [BOJ] 6359 만취한 상범 / 수학, 구현, 정수론, 시뮬레이션
for _ in range(int(input())):
    n = int(input())
    rooms = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i, n+1, i):
            if rooms[j]: rooms[j] = 0
            else: rooms[j] = 1
    print(sum(rooms[1:]))