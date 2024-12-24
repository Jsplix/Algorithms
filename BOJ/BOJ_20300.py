import sys
input = sys.stdin.readline
# [BOJ] 20300 서강근육맨 / 그리디, 정렬
n = int(input())
T = list(map(int, input().split()))
T.sort()

days = (n + 1) // 2
d = 1 if n % 2 else 0
m = T[-1] if d else 0
l, r = 0, n-2 if d else n-1
while d <= days and l != r: 
    d += 1
    temp = T[l] + T[r]

    if m < temp: m = temp
    l += 1
    r -= 1
print(m)