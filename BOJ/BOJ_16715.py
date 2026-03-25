import sys
input = sys.stdin.readline
# [BOJ] 16715 Inspiration / 수학, 브루트포스
def convert(x, base):
    ret = 0
    while x > 0:
        ret += x % base
        x //= base
    
    return ret

N = int(input())
mx = 0
last = 0
for i in range(2, N + 1):
    r = convert(N, i)
    if mx < r:
        mx = r
        last = i

print(mx, last)