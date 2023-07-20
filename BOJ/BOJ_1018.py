# [BOJ] 1018 체스판 다시 칠하기 / 브루트 포스
N, M = map(int, input().split()) # N - 세로, M - 가로

board = []

std1 = "WBWBWBWB"
std2 = "BWBWBWBW"

chess1 = [ std1, std2, std1, std2, std1, std2, std1, std2 ]
chess2 = [ std2, std1, std2, std1, std2, std1, std2, std1 ]

for i in range(N):
    board.append(input())
cnt = 32
ans = []
for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = 0
        cnt2 = 0
        new = []

        for k in range(i, i + 8):
            new.append(board[k][j: j+8])
        
        for p1 in range(8):
            for p2 in range(8):
                if new[p1][p2] != chess1[p1][p2]:
                    cnt1 += 1
                if new[p1][p2] != chess2[p1][p2]:
                    cnt2 += 1
        ans.append(min(cnt1, cnt2))

print(min(ans))