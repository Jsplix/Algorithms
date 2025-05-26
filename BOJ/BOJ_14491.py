import sys
input = sys.stdin.readline
# [BOJ] 14491 9진수 / 수학, 구현
n = int(input())
result = ''
while n:
    result += str(n % 9)
    n //= 9
print(result[::-1])