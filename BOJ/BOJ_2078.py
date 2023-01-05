import sys
input = sys.stdin.readline
# [BOJ] 2078 무한이진트리 / 수학, 트리
# 트리의 개념을 알기보다는 수학적으로 접근하는 것이 핵심인 것 같다.
a, b = map(int, input().split())

l_cnt = r_cnt = 0

while a > 1 and b > 1:
    if a > b:
        l_cnt += a // b
        a %= b
    else:
        r_cnt += b // a
        b %= a

l_cnt += a - 1
r_cnt += b - 1

print(l_cnt, r_cnt)