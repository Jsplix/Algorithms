import sys
input = sys.stdin.readline
# [BOJ] 27962 오렌지먹은지오랜지 / 구현, 문자열
# MAX_INPUT_SIZE = 2000 / 2-for-loop => O(N**2)
# time_limit = 1s / 2000**2 = 4000000 /
n = int(input())
s = input().rstrip()

for i in range(1, n + 1):
    cnt = 0
    front = s[:i]
    rear = s[len(s)-i:]
    for j in range(i):
        if front[j] != rear[j]: cnt += 1
    
    if cnt == 1: 
        print("YES")
        exit(0)
print("NO")