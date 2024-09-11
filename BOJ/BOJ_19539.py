import sys
input = sys.stdin.readline
# [BOJ] 19539 사과나무 / 수학, 그리디
n = int(input())
heights = list(map(int, input().split()))

sm = sum(heights)
check = 0
if sm % 3 == 0:
    for h in heights:
        check += (h // 2)
    
    if check >= (sm / 3):
        print("YES")
    else:
        print("NO")
else:
    print("NO")