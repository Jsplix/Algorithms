import sys
input = sys.stdin.readline
# [BOJ] 19951 태상이의 훈련소 생활 / 누적 합
# 기존의 누적 합과는 다른 방식. 구간의 양 끝에 더해줄 값을 더하고 빼주고
# 최종적으로 변화량을 dp 리스트에 저장. height에 변화량을 더해서 최종 결과를 구함.
n, m = map(int, input().split())
height = list(map(int, input().split()))

grnd = [0 for _ in range(n+1)]
for i in range(m):
    a, b, k = map(int, input().split())
    grnd[a-1] += k
    grnd[b] -= k

dp = [0 for _ in range(n+1)]
dp[0] = grnd[0]
for i in range(1, n+1):
    dp[i] = dp[i-1] + grnd[i]

for i in range(n):
    height[i] += dp[i]
print(*height)