import sys
input = sys.stdin.readline
# [BOJ] 21312 홀짝 칵테일 / 수학, 구현, 사칙연산
a, b, c = map(int, input().split())

odd = []
for x in [a, b, c]:
    if x % 2: odd.append(x)

if len(odd) == 0:
    print(a*b*c)
else: 
    result = 1
    for x in odd:
        result *= x
    print(result)