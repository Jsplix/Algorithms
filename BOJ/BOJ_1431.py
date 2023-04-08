import sys
input = sys.stdin.readline
# [BOJ] 1431 시리얼 번호 / 정렬
n = int(input())
serial_numbers = list(input().rstrip() for _ in range(n))

answer = []
for i in range(n):
    check = 0
    for c in serial_numbers[i]:
        if c.isalpha(): continue
        else: check += int(c)
    answer.append((serial_numbers[i], check))

answer.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for i in range(n):
    print(answer[i][0])