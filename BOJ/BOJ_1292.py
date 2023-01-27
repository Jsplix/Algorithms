import sys
input = sys.stdin.readline
# [BOJ] 1292 쉽게 푸는 문제 / 수학, 구현
a, b = map(int, input().split())
arr = []
for i in range(1, b + 1):
    for j in range(1, i + 1):
        arr.append(i)
print(sum(arr[a-1:b]))