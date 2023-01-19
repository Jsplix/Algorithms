import sys
input = sys.stdin.readline

# [BOJ] 1285 동전 뒤집기 / 비트마스킹, 그리디, 브루트포스

n = int(input())
table = [list(input().rstrip()) for _ in range(n)]
answer = int(2e6)
# temp에 table 복사 후 비트마스킹을 통해서 어떤 행을 뒤집을 것인지 결정
# ex) 000 - 아무것도 뒤집지 않음 / 001 - 0행 뒤집음 / 100 - 2행 뒤집음 ...
for bit in range(1 << n):
    temp = [table[i][:] for i in range(n)]
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                if temp[i][j] == 'H': temp[i][j] = 'T'
                else: temp[i][j] = 'H'

    # 뒤집고 난 후 열을 탐색하면서 'T'의 개수를 확인 'T'가 더 많으면 뒤집음
    # 'T'가 더 적은 경우 뒤집지 않음 (n-cnt는 'H'의 개수)
    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if temp[j][i] == 'T': cnt += 1
        total += min(cnt, n-cnt)
    answer = min(answer, total)

print(answer)