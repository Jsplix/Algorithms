import sys
input = sys.stdin.readline
# [BOJ] 1263 시간 관리 / 그리디, 정렬
n = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(n)]
schedules.sort(key= lambda x:(x[1]))

time = 0
while True:
    totalTime = time
    for working, finish in schedules:
        if totalTime + working <= finish:
            totalTime += working
        else:
            print(time-1)
            exit(0)
    time += 1