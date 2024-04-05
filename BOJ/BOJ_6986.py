import sys
input = sys.stdin.readline
# [BOJ] 6986 절사평균 / 구현, 정렬
FP = float(1e-6)
n, k = map(int, input().split())
scores = sorted(float(input()) for _ in range(n))

t_mean = 0.0
t_temp = 0
for i in range(k, n-k):
    t_temp += scores[i]
t_mean = t_temp / (n - (2 * k))

a_mean = 0.0
a_temp = (scores[k] * k) + (scores[n-k-1] * k)
for i in range(k, n-k):
    a_temp += scores[i]
a_mean = a_temp / n
# 부동소수점 오차로 인해 1e-6을 더해줘야 함.
# 0.5의 경우 0.499999999999999와 같이 저장이되어 1이 아닌 0으로 반올림되기 때문.
if k == 0: print("%0.2f\n%0.2f" % (sum(scores) / n, sum(scores) / n))
else: print("%0.2f\n%0.2f" % (t_mean + FP, a_mean + FP))