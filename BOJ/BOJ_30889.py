import sys
input = sys.stdin.readline
# [BOJ] 30889 좌석 배치도 / 구현, 문자열
seats = [['.' for _ in range(20)] for _ in range(10)]
for _ in range(int(input())):
    s = input().rstrip()
    r, c = s[0], int(s[1:])
    seats[ord(s[0])-ord('A')][c-1] = 'o'
print('\n'.join([''.join(r) for r in seats]))