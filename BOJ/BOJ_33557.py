import sys
input = sys.stdin.readline
# [BOJ] 33557 곱셈을 누가 이렇게 해 ㅋㅋ / 수학, 구현, 문자열, 사칙연산
for _ in range(int(input())):
    a, b = input().split()

    r = int(a) * int(b)
    v = ''
    if len(a) == len(b):
        for i in range(len(a)):
            v += str(int(a[i]) * int(b[i]))
    else:
        l = a if len(a) >= len(b) else b
        s = a if len(a) < len(b) else b

        diff = len(l) - len(s)
        v += l[:diff]
        for i in range(diff, len(l)):
            v += str(int(l[i]) * int(s[i - diff]))

    print(1 if r == int(v) else 0)