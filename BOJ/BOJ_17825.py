import sys
input = sys.stdin.readline
# [BOJ] 17825 주사위 윷놀이 / 구현, 브루트포스, 시뮬레이션, 백트래킹

# 다음 갈 위치를 저장
position = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 24], [12],
            [13], [14], [15], [16, 26], [17], [18], [19], [20], [32], [22], [23], [29], [25], [29],
            [27], [28], [29], [30], [31], [20], [32]]

# 위치 별 점수
scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
          13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]

def back(turn, temp):
    global mx
    if turn == 10:
        mx = max(mx, temp)
        return
    
    for i in range(4):
        start = horses[i]
        cur = position[start][-1]
        for _ in range(1, sequences[turn]):
            cur = position[cur][0]
        
        if cur == 32 or cur not in horses:
            horses[i] = cur
            back(turn + 1, temp + scores[cur])
            horses[i] = start

sequences = list(map(int, input().split()))
mx = -1
horses = [0, 0, 0, 0]

back(0, 0)
print(mx)