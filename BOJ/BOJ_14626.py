import sys
input = sys.stdin.readline
# [BOJ] 14626 ISBN / 수학, 구현, 브루트포스, 사칙연산
isbn = list(input().rstrip())

val = 0
idx = -1
for i in range(len(isbn)):
    if isbn[i] == '*': idx = i; continue
    val += int(isbn[i]) if i % 2 == 0 else int(isbn[i]) * 3

if idx % 2 == 0:
    for x in range(10):
        if (val + x) % 10 == 0:
            print(x)
            break
else:
    for x in range(10):
        if (val + (3 * x)) % 10 == 0:
            print(x)
            break