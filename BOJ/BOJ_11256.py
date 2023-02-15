import sys
input = sys.stdin.readline
# [BOJ] 11256 사탕 / 그리디, 정렬
for _ in range(int(input())):
    j, n = map(int, input().split())
    box = [tuple(map(int, input().split())) for _ in range(n)]
    box.sort(key=lambda x:-(x[0]*x[1]))
    
    cnt = 0
    for i in range(n):
        if box[i][0]*box[i][1] > j:
            cnt += 1
            break
        elif box[i][0]*box[i][1] <= j:
            j -= box[i][0]*box[i][1]
            cnt += 1
            if j == 0:
                break
    print(cnt)