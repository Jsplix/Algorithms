import sys
input = sys.stdin.readline
# [BOJ] 2480 윷놀이 / 구현
result = {4: "E", 3: "A", 2: "B", 1: "C", 0: "D"}
for _ in range(3):
    sm = sum(list(map(int, input().split())))
    print(result[sm ])