import sys
input = sys.stdin.readline
# [BOJ] 16713 Generic Queries / 누적 합
n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
accum = [0 for _ in range(n+1)]

for i in range(1, n+1):
    accum[i] = arr[i] ^ accum[i-1]

answer = 0
for _ in range(q):
    s, e = map(int, input().split())
    answer ^= (accum[e] ^ accum[s-1])
print(answer)