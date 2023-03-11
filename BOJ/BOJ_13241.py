import sys
input = sys.stdin.readline
# [BOJ] 13241 최소공배수 / 수학, 정수론, 유클리드 호제법
a, b = map(int, input().split())
result = a*b

while b:
    if a > b: a, b = b, a
    b %= a

print(result // a)