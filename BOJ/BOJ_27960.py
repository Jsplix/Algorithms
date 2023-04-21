import sys
input = sys.stdin.readline
# [BOJ] 27960 사격 내기 / 수학, 비트마스킹
point = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
sa, sb = map(int, input().split())
c_point = 0
for p in point:
    a_flag, b_flag = False, False
    if sa >= p:
        sa -= p
        a_flag = True
    if sb >= p:
        sb -= p
        b_flag = True

    if (a_flag and b_flag) or (not a_flag and not b_flag):
        continue
    else:
        c_point += p

print(c_point)