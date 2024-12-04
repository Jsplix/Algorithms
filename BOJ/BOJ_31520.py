import sys
input = sys.stdin.readline
# [BOJ] 31520 Champernowne Verification / 수학, 구현
def is_champernowne(n):
    cnt = 1
    temp = ''
    while len(n) != len(temp):
        temp += str(cnt)
        if n[:len(temp)] != temp:
            return -1
        cnt += 1
    cnt -= 1
    if temp == n:
        return cnt
    else:
        return -1

n = input().rstrip()
print(is_champernowne(n))