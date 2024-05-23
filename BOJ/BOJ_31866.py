import sys
input = sys.stdin.readline
# [BOJ] 31866 손가락 게임 / 구현, 많은 조건 분기
a, b = map(int, input().split())
mp = {0: "rock", 1: "x", 2: "scissors", 3: "x", 4: "x", 5: "paper"}
js, ij = mp[a], mp[b]

if js != "x" and ij != "x":
    if js == "rock":
        if ij == "rock": print("=")
        elif ij == "scissors": print(">")
        else: print("<")
    elif js == "scissors": 
        if ij == "rock": print("<")
        elif ij == "scissors": print("=")
        else: print(">")
    else:
        if ij == "rock": print(">")
        elif ij == "scissors": print("<")
        else: print("=")
else:
    if js == "x" and ij == "x":
        print("=")
    else:
        print(">" if js != "x" else "<")