import sys
import math
input = sys.stdin.readline
# [BOJ] 3036 링 / 수학, 정수론, 유클리드 호제법
# 기약분수는 분모, 분자의 최대공약수를 구해서 각각 나눠주면 된다
# ex) (분자 / 최대공약수) / (분모 / 최대공약수)
n = int(input())
r = list(map(int, input().split()))
ans_c = [0 for _ in range(n)]
ans_p = [0 for _ in range(n)]
for i in range(1, n):
    ans_c[i] = r[0] // math.gcd(r[i], r[0])
    ans_p[i] = r[i] // math.gcd(r[i], r[0])

for i in range(1, n):
    print(str(ans_c[i]) + "/" + str(ans_p[i]))