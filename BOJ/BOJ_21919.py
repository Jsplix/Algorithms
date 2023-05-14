import sys
input = sys.stdin.readline
# [BOJ] 21919 소수 최소 공배수 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
MAX = 1000000
sieve = [1 for _ in range(MAX+1)]
sieve[0], sieve[1] = 0, 0

for i in range(2, int(MAX**0.5) + 1):
    if sieve[i]:
        for j in range(i+i, MAX+1, i):
            sieve[j] = 0

n = int(input())
arr = list(map(int, input().split()))
arr = list(set(arr))
p_lcm = 1

for i in range(len(arr)):
    if sieve[arr[i]]: p_lcm *= arr[i]

if p_lcm == 1: print(-1)
else: print(p_lcm)