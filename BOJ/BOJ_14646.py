import sys
input = sys.stdin.readline
# [BOJ] 14646 욱제는 결정장애야!! / 구현, 시뮬레이션
n = int(input())
menu_num = list(map(int, input().split()))
board_dict = {i:0 for i in range(1, n+1)}

sticker_cnt = 0
mx = 0
for mn in menu_num:
    if not board_dict[mn]: sticker_cnt += 1; board_dict[mn] = 1
    else: sticker_cnt -= 1
    mx = max(mx, sticker_cnt)
print(mx)