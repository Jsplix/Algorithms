import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if arr != []:
            print(min(arr))
            arr.pop(arr.index(min(arr)))
        else:
            print(0)
    else:
        arr.append(x)