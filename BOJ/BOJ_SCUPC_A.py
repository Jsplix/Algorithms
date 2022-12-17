import sys
input = sys.stdin.readline

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