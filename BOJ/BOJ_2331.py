import sys
input = sys.stdin.readline
# [BOJ] 2331 반복수열 / 수학, 구현
a, p = map(int, input().split())
d = [a]

idx = 0
while True:
    val = 0
    for c in str(d[idx]):
        val += int(c)**p
    
    if val in d: cut = d.index(val); break
    d.append(val)
    idx += 1
    
print(len(d[:cut]))