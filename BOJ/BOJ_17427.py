import sys
input = sys.stdin.readline
# [BOJ] 17427 약수의 합 2 / 수학, 정수론
n = int(input())
answer = 0
for x in range(1, n+1):
    answer += (n//x)*x
print(answer)
# [BOJ] 1676 과 동일한 메커니즘. n / i (i는 자연수) 는 n에서 i의 약수의 개수이다.