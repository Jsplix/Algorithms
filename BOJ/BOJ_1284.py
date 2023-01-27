import sys
input = sys.stdin.readline
# [BOJ] 1284 집 주소 / 수학, 구현
std = {0: 4, 1: 2, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3}
while 1:
    n = list(map(str, input().rstrip()))
    if len(n) == 1 and int(n[0]) == 0:
        break
    board_len = 1
    for x in n:
        board_len += std[int(x)] + 1
    print(board_len)