import sys
input = sys.stdin.readline
# [BOJ] 1551 수열의 변화 / 수학, 구현, 문자열, 시뮬레이션, 파싱
N, K = map(int, input().split())
arr = list(map(int, input().split(',')))

for i in range(1, K + 1):
    for j in range(N - i):
        arr[j] = arr[j + 1] - arr[j]

print(*arr[:N - K], sep=',')