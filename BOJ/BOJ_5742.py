import sys
input = sys.stdin.readline
# [BOJ] 5742 Weekend Lottery / 구현
while True:
    n, c, k = map(int, input().split())

    if n == 0 and c == 0 and k == 0: break
    numbers = {i: 0 for i in range(1, k+1)}

    for _ in range(n):
        for x in list(map(int, input().split())):
            numbers[x] += 1
    
    result = list(numbers.items())
    result.sort(key=lambda x:x[1])

    mn = result[0][1]
    answer = [result[0][0]]
    for key, value in result[1:]:
        if value == mn: answer.append(key)
        else: break
    
    print(*answer)