import sys
input = sys.stdin.readline
# [BOJ] 2435 기상청 인턴 신현수 / 브루트포스, 누적 합
n, k = map(int, input().split())
temperature = list(map(int, input().split()))

mx = -10001
for i in range(n-k+1):
    mx = max(mx, sum(temperature[i:i+k]))
print(mx)