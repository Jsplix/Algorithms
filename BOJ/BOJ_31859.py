import sys
input = sys.stdin.readline
# [BOJ] 31859 SMUPC NAME / 구현, 문자열
chk = {chr(i):0 for i in range(ord('a'), ord('z')+1)}
n, s = input().rstrip().split()
n = int(n)
s = list(s)

discard = []
for i in range(len(s)):
    if not chk[s[i]]: 
        chk[s[i]] = 1
    else:
        discard.append(i)

discard_num = len(discard)
p_cnt = 0
for d in discard:
    s.pop(d-p_cnt)
    p_cnt += 1

answer = str(1906 + n) + ''.join(s) + str(discard_num + 4)
answer = 'smupc_' + answer[::-1]
print(answer)