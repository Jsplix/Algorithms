import sys
input = sys.stdin.readline
# [BOJ] 11292 키 큰 사람 / 구현, 정렬
while True:
    n = int(input())
    record = []
    if n == 0: break
    for idx in range(n):
        name, height = input().split()
        height = float(height)
        record.append((name, height, idx))
    record.sort(key=lambda x: (-x[1], x[2]))
    answer = ''
    for i in range(n):
        if i == 0: answer += record[i][0]
        else:
            if record[i][1] == record[i-1][1]:
                answer += ' '
                answer += record[i][0]
            else: break
    print(answer)