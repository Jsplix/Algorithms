import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 1270 전쟁 - 땅따먹기 / 구현, 자료 구조, 해시 사용한 집합과 맵, 보이어-무어 다수결 투표
for _ in range(int(input())):
    check = defaultdict(int)
    t, *army = map(int, input().split())

    for i in range(t):
        check[army[i]] += 1
    
    result = list(check.items())
    result.sort(key= lambda x: -x[1])

    if result[0][1] > t // 2: print(result[0][0])
    else: print("SYJKGW")