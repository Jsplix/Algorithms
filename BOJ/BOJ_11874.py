import sys
input = sys.stdin.readline
# [BOJ] 11874 ZAMKA / 수학, 브루트포스
l = int(input())
d = int(input())
x = int(input())

mx = -1
mn = 10001
for i in range(l, d+1):
    temp = sum(list(map(int, str(i))))
    if temp == x: 
        mx = max(mx, i)
        mn = min(mn, i)

print(mn)
print(mx)