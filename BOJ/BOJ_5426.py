import sys
input = sys.stdin.readline
# [BOJ] 5426 비밀 편지 / 수학, 구현, 문자열
for _ in range(int(input())):
    letter = input().rstrip()
    let_len = len(letter)
    r = 0

    mtrx = [[] for _ in range(int(let_len**0.5))]
    for i in range(let_len):
        if i % int(let_len**0.5) == 0 and i != 0: r += 1
        mtrx[r].append(letter[i])

    let = ''
    for i in range(int(let_len**0.5)-1, -1, -1):
        for j in range(int(let_len**0.5)):
            let += mtrx[j][i]
    
    print(let)