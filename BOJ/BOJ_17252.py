import sys
input = sys.stdin.readline
# [BOJ] 17252 삼삼한 수 / 수학, 사칙연산
x = int(input())
now = 0
check = []

if x == 0: 
    print("NO")
    exit(0)

while 3**now <= x:
    check.append(3**now)
    now += 1

for i in range(len(check)-1, -1, -1):
    if x >= check[i]:
        x -= check[i]

if x: print("NO")
else: print("YES")