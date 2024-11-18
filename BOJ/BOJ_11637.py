import sys
input = sys.stdin.readline
# [BOJ] 11637 인기 투표 / 구현
for _ in range(int(input())):
    votes = [int(input()) for _ in range(int(input()))]
    mx_votes = max(votes)

    if votes.count(mx_votes) >= 2: print("no winner")
    else:
        idx = votes.index(mx_votes) + 1
        print("majority winner %d" % idx) if sum(votes) - mx_votes < mx_votes else print("minority winner %d" % idx)