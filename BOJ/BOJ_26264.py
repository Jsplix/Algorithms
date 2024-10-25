import sys
input = sys.stdin.readline
# [BOJ] 26264 빅데이터? 정보보호! / 문자열
n = int(input())
q = input().rstrip()

b_cnt = q.count('bigdata')
s_cnt = q.count('security')

if b_cnt == s_cnt:
    print("bigdata? security!")
elif b_cnt > s_cnt:
    print("bigdata?")
else:
    print("security!")