import sys
input = sys.stdin.readline
# [BOJ] 15701 순서쌍 / 수학, 정수론
n = int(input())

count = 0
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        count += 1
        if i ** 2 != n:
            count += 1

print(count)