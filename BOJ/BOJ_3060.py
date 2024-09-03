import sys
input = sys.stdin.readline
# [BOJ] 3060 욕심쟁이 돼지 / 수학, 구현, 시뮬레이션
for _ in range(int(input())):
    n = int(input())
    eat = sum(list(map(int, input().split())))
    
    day = 1
    while n >= eat:
        eat *= 4
        day += 1
    print(day)