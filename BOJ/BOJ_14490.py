import sys
input = sys.stdin.readline
# [BOJ] 14490 백대열 / 수학, 문자열, 정수론, 유클리드 호제법
def Euclidean(a, b):
    r = b % a
    if r == 0: return a
    return Euclidean(r, a)

n, m = map(int, input().split(':'))
q = Euclidean(n, m)
print(n//q, ':', m//q, sep='')