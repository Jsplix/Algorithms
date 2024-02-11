import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2785 체인 / 그리디, 정렬
n = int(input())
chains = deque(sorted(list(map(int, input().split()))))

answer = 0
while len(chains) != 1:
    chains[0] -= 1
    left = chains.pop()
    right = chains.pop()
    chains.append(left+right)
    answer += 1

    if chains[0] == 0:
        chains.popleft()

print(answer)