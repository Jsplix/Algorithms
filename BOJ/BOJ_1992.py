import sys
input = sys.stdin.readline
# [BOJ] 1992 쿼드트리 / 분할 정복, 재귀
# 2630 색종이 만들기 문제의 재귀 함수와 형식이 거의 똑같음
def solve(x, y, N): 
    global white, black, answer
    if N == 0: return 0
    temp = 0
    for i in range(y, y + N):
        for j in range(x, x + N):
            if board[i][j] == 1:
                temp += 1
    if not temp:
        answer += '0'
    elif temp == N**2:
        answer += '1'
    else: # 함수를 호출하기 전에 괄호를 추가
        answer += '('
        solve(x, y, N//2)
        solve(x + N//2, y, N//2)
        solve(x, y + N//2, N//2)
        solve(x + N//2, y + N//2, N//2)
        answer += ')'
    return

n = int(input())
board = []
answer = '' # 문자열로 선언해줌 (출력 및 답을 저장하기에 용이함)
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

white, black = 0, 0
solve(0, 0, n)
print(answer)