import sys
input = sys.stdin.readline
# [BOJ] 1100 하얀 칸 - 구현, 문자열
odd_line = ["W", "B", "W", "B", "W", "B", "W", "B"]
even_line = ["B", "W", "B", "W", "B", "W", "B", "W"]
input_board = []

for _ in range(8):
    input_board.append(list(map(str, input().rstrip())))

cnt = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 1:
            if input_board[i][j] == 'F' and even_line[j] == 'W':
                cnt += 1
        else:
            if input_board[i][j] == 'F' and odd_line[j] == 'W':
                cnt += 1

print(cnt)