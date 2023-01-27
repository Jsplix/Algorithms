import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
chk = ['H', 'I', 'A', 'R', 'C']
ans = [0, 0, 0, 0, 0]
for c in s:
    if c in chk:
        ans[chk.index(c)] += 1
print(min(ans))