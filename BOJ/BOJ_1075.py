import sys
input = sys.stdin.readline
# [BOJ] 1075 나누기 / 수학, 브루트 포스
n = int(input())
f = int(input())

chk = []
for i in range(99):
    if (n+i)//100 > n//100: break
    if (n+i)%f == 0: chk.append((n+i)%100)

for i in range(99):
    if (n-i)//100 < n//100: break
    if (n-i)%f == 0: chk.append((n-i)%100)

chk.sort()
answer = ''

if len(str(chk[0])) == 1:
    answer = '0' + str(chk[0])
else:
    answer = str(chk[0])
print(answer)