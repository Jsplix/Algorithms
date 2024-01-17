import sys
input = sys.stdin.readline
# [BOJ] 1188 음식 평론가 / 수학, 정수론, 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

n, m = map(int, input().split())
print(m - gcd(n, m))