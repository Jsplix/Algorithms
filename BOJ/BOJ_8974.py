import sys
input = sys.stdin.readline
# [BOJ] 8974 희주의 수학시험 / 수학, 구현, 사칙연산
a, b = map(int, input().split())

arr = []
for i in range(1, 1000):
    for j in range(1, i+1):
        arr.append(i)

print(sum(arr[a-1:b]))