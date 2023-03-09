import sys
input = sys.stdin.readline
# [BOJ] 1969 DNA / 구현, 문자열, 그리디, 브루트 포스
n, m = map(int, input().split())
dna = []
for _ in range(n):
    dna.append(input().rstrip())
        
cnt = 0
result = ''
for i in range(m):
    count = [0, 0, 0, 0]  # A, C, G, T 개수
    for j in range(n):
        if dna[j][i] == 'A':
            count[0] += 1
        elif dna[j][i] == 'C':
            count[1] += 1
        elif dna[j][i] == 'G':
             count[2] += 1
        elif dna[j][i] == 'T':
            count[3] += 1
    mx_idx = count.index(max(count))
    if mx_idx == 0:
        result += 'A'
    elif mx_idx == 1:
        result += 'C'
    elif mx_idx == 2:
         result += 'G'
    elif mx_idx == 3:
        result += 'T'
    cnt += n - max(count)

print(result)
print(cnt)