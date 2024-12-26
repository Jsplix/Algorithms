import sys
input = sys.stdin.readline
# [BOJ] 32941 왜 맘대로 예약하냐고 / 구현, 브루트포스
t, x = map(int, input().split())
flag = False
for _ in range(int(input())):
    k = int(input())
    possible = list(map(int, input().split()))
    if x not in possible: flag = True
print("YES" if not flag else "NO")