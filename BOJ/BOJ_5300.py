import sys
input = sys.stdin.readline
# [BOJ] 5300 Fill the Rowboats! / 구현
res = [i for i in range(int(input())+1)]
for i in range(1, len(res)):
    print(i, end=" ")
    if i % 6 == 0: print("Go!", end=" ")

if (len(res)-1) % 6 != 0: print("Go!")