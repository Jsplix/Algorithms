import sys
input = sys.stdin.readline
# [BOJ] 1850 최대공약수 / 수학, 정수론, 유클리드 호제법
a, b = map(int, input().split())
# a, b는 1의 길이를 나타내지만 결국, a와 b의 최대 공약수가 정답의 '1'의 개수임
def Euclidean(a, b):
    r = b % a
    if r == 0: return a
    return Euclidean(r, a)

print(Euclidean(a, b)*'1')