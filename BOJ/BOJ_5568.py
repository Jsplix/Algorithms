from itertools import permutations
import sys
input = sys.stdin.readline
# [BOJ] 5568 카드 놓기 / 자료 구조, 브루트 포스, 해시 사용 집합과 맵
n = int(input())
k = int(input())
cards = [input().rstrip() for _ in range(n)]
perm = set(permutations(cards, k))

answer = []
# 카드 상으로는 중복이 되지 않지만, 합쳐서 수를 만들 경우 중복이 되는 경우도 있음.
for p in perm:
    answer.append(''.join(p))

print(len(set(answer)))