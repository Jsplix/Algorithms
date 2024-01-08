import sys
input = sys.stdin.readline
# [BOJ] 1106 호텔 / DP, 배낭 문제, Knapsack(냅색)
# 딕셔너리로 풀어서 계속 틀렸음. 반례를 찾진 못했으나 문제 조건에서 비용이 중복되지 않는다는 말이 없음
# 즉, 중복된 비용이 들어온 경우에 딕셔너리를 사용하면 기존의 비용 대비 홍보효과가 사라지게 됨.
# 딕셔너리를 사용하면 안되는 문제라고 판단됨.
MX = int(1e6) + 1
c, n = map(int, input().split())
dp = [MX for _ in range(c+100)]
cp = [list(map(int, input().split())) for _ in range(n)]

dp[0] = 0   
for j in range(n):
    cost = cp[j][0]
    people = cp[j][1]
    for i in range(people, c+100):
        dp[i] = min(dp[i], dp[i-people] + cost)

print(*dp[c:])
print(min(dp[c:]))