import sys
input = sys.stdin.readline
# [BOJ] 1439 뒤집기 / 문자열, 그리디
# 문자열은 100만이므로 각각의 문자를 하나하나 확인해서 이전과 문자가 다른 경우만 cnt 수를 1증가
# 마지막에 최종적으로 더 적은 값을 출력
s = input().rstrip()
z_cnt, o_cnt = (1, 0) if s[0] == '0' else (0, 1)
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0': z_cnt += 1
        else: o_cnt += 1

print(min(z_cnt, o_cnt))