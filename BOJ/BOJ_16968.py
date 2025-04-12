import sys
input = sys.stdin.readline
# [BOJ] 16968 차량 번호판 1 / 수학, 조합론
form = input().rstrip()

result = 1
prev = ''
for f in form:
    if f == 'd':
        if prev == 'd': result *= 9
        else: result *= 10
    else:
        if prev == 'c': result *= 25
        else: result *= 26
    prev = f

print(result)