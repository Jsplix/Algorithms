import sys
input = sys.stdin.readline
# [BOJ] 34534 Form a Straight! / 구현, 브루트포스
cards = set(map(int, input().split()))
case = []
for i in range(1, 6):
    case.append(set([i, i + 1, i + 2, i + 3, i + 4]))

mn = 6
for i in range(5):
    mn = min(mn, 5 - len(cards.intersection(case[i])))
print(mn)