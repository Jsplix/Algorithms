import sys
input = sys.stdin.readline
# [BOJ] 5355 화성 수학 / 수학, 구현, 사칙연산
for _ in range(int(input())):
    op = list(input().split())
    val = float(op[0])
    for c in op[1:]:
        if c == '@': val *= 3
        elif c == '%': val += 5
        elif c == '#': val -= 7
    
    print("%.2f" % val)