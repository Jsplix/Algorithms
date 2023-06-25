import sys
input = sys.stdin.readline
# [BOJ] 20310 타노스 / 문자열, 그리디
# 핵심: 순서 유지, 사전순 정렬 - 0이 최대한 앞에 있어야 하므로 뒤에서부터 0 제거, 1은 앞에서부터 제거
s = list(input().rstrip())
zero_cnt = s.count('0') // 2
one_cnt = s.count('1') // 2
idx = 0

s = s[::-1]
while zero_cnt:
    if s[idx] == '0':
        s.pop(idx)
        zero_cnt -= 1
        idx = 0
    else:
        idx += 1

s = s[::-1]
while one_cnt:
    if s[idx] == '1':
        s.pop(idx)
        one_cnt -= 1
        idx = 0
    else:
        idx += 1

print(''.join(s))