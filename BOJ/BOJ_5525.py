import sys
input = sys.stdin.readline
# [BOJ] 5525 IOIOI / 문자열
n = int(input())
m = int(input())
s = input().rstrip()

cnt, chk, cur = 0, 0, 1
while cur < m - 1: # != 과 < 연산의 처리 시간은 매우 차이가 남. (<로 하면 통과가 되었음..)
    if s[cur-1] == 'I' and s[cur] == 'O' and s[cur+1] == 'I':
        chk += 1
        if chk == n:
            chk -= 1
            cnt += 1
        cur += 1
    else: chk = 0
    cur += 1
print(cnt)