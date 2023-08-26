from itertools import permutations
import sys
input = sys.stdin.readline
# [BOJ] 2992 크면서 작은 수 / 문자열, 브루트포스, 백트래킹
x = input().rstrip()
chk = list(set(permutations(x, len(x))))

answer = []
for p in chk:
    answer.append(int(''.join(p)))

answer.sort()
idx = answer.index(int(x))
if idx == len(answer)-1:
    print(0)
else:
    print(answer[idx+1])