import sys
input = sys.stdin.readline
# [BOJ] 32400 다트판 / 수학, 구현, 사칙연산
scores = list(map(int, input().split()))
alice = 0
bob = 10.5

for i in range(20):
    if scores[i] == 20:
        alice += scores[i] 
        if i == 0: alice += (scores[i+1] + scores[-1])
        elif i == 19: alice += (scores[i-1] + scores[0])
        else: alice += (scores[i-1] + scores[i+1])
        break

alice /= 3
if alice < bob: print("Bob")
elif alice > bob: print("Alice")
else: print("Tie")