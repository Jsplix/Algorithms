import sys
input = sys.stdin.readline
p = []
for _ in range(10):
    p.append(float(input()))
p.sort()
tp = 10**9
for i in range(9):
    tp *= (p[i + 1] / (i + 1))
print("{:.6f}" .format(tp))