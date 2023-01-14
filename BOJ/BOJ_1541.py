import sys
input = sys.stdin.readline
# [BOJ] 1541 잃어버린 괄호 / 그리디, 문자열, 파싱

f = input().rstrip().split('-')
n = []
for i in range(len(f)):
    chk = 0
    f[i] = list(f[i].split('+'))
    for x in f[i]:
        chk += int(x)
    n.append(chk)

ans = n[0]
for i in range(1, len(n)):
    ans -= n[i]
print(ans)