import sys
input = sys.stdin.readline
# [BOJ] 11497 통나무 건너뛰기 / 정렬, 그리디
for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    answer = 0
    for i in range(2, n):
        answer = max(answer, abs(arr[i]-arr[i-2]))
    print(answer)