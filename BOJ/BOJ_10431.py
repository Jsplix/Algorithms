import sys
input = sys.stdin.readline
# [BOJ] 10431 줄세우기 / 구현, 정렬, 시뮬레이션
for _ in range(int(input())):
    tc, *heights = map(int, input().split())
    move_count = 0
    sorted_heights = []
    for h in heights:
        if not sorted_heights or sorted_heights[-1] < h:
            sorted_heights.append(h)
            continue
        
        for i in range(len(sorted_heights)):
            if sorted_heights[i] > h:
                sorted_heights.insert(i, h)
                move_count += len(sorted_heights) - (i + 1)
                break
            
    print(tc, move_count)