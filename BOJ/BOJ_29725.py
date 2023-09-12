from curses.ascii import isupper
import sys
input = sys.stdin.readline
# [BOJ] 29725 체스 초보 브실이 / 구현
things = {'K': 0, 'k': 0, 'p': 1, 'P': 1, 'N': 3, 'n': 3, 'B': 3, 'b': 3, 'R': 5, 'r': 5, 'Q': 9, 'q': 9} 
wt, bk = 0, 0

for _ in range(8):
    for c in input().rstrip():
        if c == '.': continue
        if c.isupper():
            wt += things[c]
        else:
            bk += things[c]
print(wt-bk)