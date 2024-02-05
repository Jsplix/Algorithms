import sys
input = sys.stdin.readline
# [BOJ] 17828 문자열 화폐 / 그리디, 문자열
n, x = map(int, input().split())
if x < n or x > 26 * n: print("!")
else:
    answer = ['A' for _ in range(n)]
    x -= n
    i = n - 1

    while x:
        if x >= 25:
            answer[i] = 'Z'
            i -= 1
            x -= 25 # 기존의 값이 'A'(1) 이므로 'Z'를 뺄 수 있는 경우 추가로 25만 더 빼주면 됨
        else:
            answer[i] = chr(x + ord('A'))
            x = 0
    print(''.join(answer))