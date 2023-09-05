import sys
input = sys.stdin.readline
# [BOJ] 먹을 것인가 먹힐 것인가 / 정렬, 이분 탐색, 투 포인터
for _ in range(int(input())):
    a_size, b_size = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())))
    
    answer, a_idx, b_idx = 0, 0, b_size-1
    while b_idx != -1 and a_idx != a_size:
        if a[a_idx] > b[b_idx]: 
            answer += b_idx + 1
            a_idx += 1
        else: 
            b_idx -= 1
    print(answer)