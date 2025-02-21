import sys
input = sys.stdin.readline
# [BOJ] 9047 6174 / 구현, 문자열, 정렬, 시뮬레이션
for _ in range(int(input())):
    num = list(input().rstrip())

    count = 0
    while ''.join(num) != '6174':
        mx = int(''.join(sorted(num)[::-1]))
        mn = int(''.join(sorted(num)))
        temp = mx - mn
        str_temp = str(temp)
        num = list('0' * (4-len(str_temp)) + str_temp)
        count += 1
    print(count)