import sys
input = sys.stdin.readline
# [BOJ] 25191 치킨댄스를 추는 곰곰이를 본 임스 / 수학, 사칙연산
n = int(input())
a, b = map(int, input().split())

coke = a // 2
beer = b // 1

if n >= coke + beer: print(coke + beer)
else: print(n)