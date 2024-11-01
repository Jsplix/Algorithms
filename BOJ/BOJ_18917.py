import sys
input = sys.stdin.readline
# [BOJ] 18917 수열과 쿼리 38 / 수학, 구현
check, result = 0, 0
for _ in range(int(input())):
    comm = list(map(int, input().split()))
    
    if comm[0] == 1:
        check += comm[1]
        result ^= comm[1]
    elif comm[0] == 2:
        check -= comm[1]
        result ^= comm[1]
    elif comm[0] == 3:
        print(check)
    elif comm[0] == 4:
        print(result)