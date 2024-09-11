import sys
input = sys.stdin.readline
# [BOJ] 27919 UDPC 파티 / 그리디
vote = input().rstrip()
cu_count, dp_count = 0, 0

for v in vote:
    if v == 'U' or v == 'C':
        cu_count += 1
    elif v == 'D' or v == 'P':
        dp_count += 1

selected = ''

if cu_count > (dp_count + 1) // 2:
    selected += 'U'

if dp_count > 0:
    selected += 'DP'

print(selected)