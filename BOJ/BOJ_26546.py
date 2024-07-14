import sys
input = sys.stdin.readline
# [BOJ] 26546 REVERSE / 구현, 문자열
for _ in range(int(input())):
    word, f, s = input().split()
    f = int(f)
    s = int(s)
    for i in range(len(word)):
        if f <= i < s: continue
        print(word[i], end='')
    print()