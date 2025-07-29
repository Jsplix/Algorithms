import sys
input = sys.stdin.readline
# [BOJ] 33541 2025는 무엇이 특별할까? / 브루트포스, 수학
x = input().rstrip()

flag = False
for i in range(int(x)+1, 10000):
    a = int(str(i)[:2])
    b = int(str(i)[2:])
    if i == (a + b) ** 2:
        print(i)
        flag = True
        break

if not flag: print(-1)