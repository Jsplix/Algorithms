import sys
input = sys.stdin.readline
# [BOJ] 14469 소가 길을 건너는 이유 3 / 그리디, 정렬
n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()

answer = time[0][0] + time[0][1]
for i in range(1, n):
    if answer < time[i][0]:
        answer = time[i][0]
        answer += time[i][1]
    else:
        answer += time[i][1]
print(answer)