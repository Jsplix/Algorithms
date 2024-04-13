import sys
input = sys.stdin.readline
# [BOJ] 2774 아름다운 수 / 구현
for _ in range(int(input())):
    x = input().rstrip()
    num = set()
    for ch in x:
        num.add(ch)
    
    print(len(num))