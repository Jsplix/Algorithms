import sys
input = sys.stdin.readline
# [BOJ] 14709 여우 사인 / 구현
finger = [[] for _ in range(6)]
for _ in range(int(input())):
    f1, f2 = map(int, input().split())
    finger[f1].append(f2)
    finger[f2].append(f1)

if (3 in finger[1] and 4 in finger[1]) and (1 in finger[3] and 4 in finger[3]) and (1 in finger[4] and 3 in finger[4]):
    if (2 in finger[1]) or (5 in finger[1]) or (2 in finger[3]) or (5 in finger[3]) or (2 in finger[4]) or (5 in finger[4]):
        print("Woof-meow-tweet-squeek")
    else:
        print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")