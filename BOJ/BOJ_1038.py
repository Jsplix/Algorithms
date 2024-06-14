import sys
input = sys.stdin.readline
# [BOJ] 1038 감소하는 수 / 브루트포스, 백트래킹
# 1자리 수는 모두 감소하는 수 0~9
# 무조건 연속하는 수가 작아야 함.
# 10, 20 21, 30 31 32, 40 41 42 43, 50 51 52 53 54, 60 61 62 63 64 65, ...
# 뒤에 숫자를 덧 붙인다. / 가장 마지막 수 - 9876543210
n = int(input())
result = [[] for _ in range(11)] 
result[1] = [i for i in range(10)]

cnt = 9
r, c = 1, n
for i in range(2, 11):
    if n <= cnt: break
    r = i
    c = -1
    for j in range(len(result[i-1])):
        chk = result[i-1][j] % 10
        for k in range(chk):
            result[i].append(result[i-1][j] * 10 + k)
            cnt += 1
            c += 1
            if cnt == n: break
        if cnt == n: break

print(result[r][c] if n <= cnt else -1)