import sys
input = sys.stdin.readline
# [BOJ] 27961 고양이는 많을수록 좋다 / 수학, 그리디
sys.setrecursionlimit(10**6)
n = int(input())

def back(now, cnt):
    global n
    if now > n: return
    if now == n:
        print(cnt)
        exit(0)
    
    back(now*2 if n - now >= now else n, cnt+1)

if n == 0: print(0)
else: back(1, 1)