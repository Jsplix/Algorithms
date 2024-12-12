import sys
input = sys.stdin.readline
# [BOJ] 1417 국회의원 선거 / 구현, 자료 구조, 그리디, 시뮬레이션, 우선순위 큐
n = int(input())
d = int(input())
votes = [int(input()) for _ in range(n-1)]

answer = 0
while n != 1 and d <= max(votes):
    d += 1
    votes[votes.index(max(votes))] -= 1
    answer += 1
print(answer)