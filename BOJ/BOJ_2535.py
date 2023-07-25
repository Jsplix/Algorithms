import sys
input = sys.stdin.readline
# [BOJ] 2535 아시아 정보올림피아드 / 구현, 정렬
record = []
for _ in range(int(input())):
    record.append(list(map(int, input().split())))

record.sort(key=lambda x:(-x[2]))

country = {}
cnt, idx = 0, 0
while cnt != 3:
    if record[idx][0] not in country.keys():
        country[record[idx][0]] = 1
    else:
        if country[record[idx][0]] == 2:
            idx += 1
            continue
        country[record[idx][0]] += 1
    
    print(*record[idx][:2])
    cnt += 1
    idx += 1