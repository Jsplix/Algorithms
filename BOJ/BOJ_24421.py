import sys
input = sys.stdin.readline
# [BOJ] 24421 掛け算 (Multiplication) / 수학, 구현, 브루트포스
n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(n - 2):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            temp = arr[i] * arr[j]
            if temp == arr[k]:
                result += 1

print(result)